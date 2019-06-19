from service_spec.LanguageDetection_pb2_grpc import LanguageDetectStub
from service_spec.LanguageDetection_pb2 import Input, Output
import unittest
import start_service
import grpc
from google.protobuf.json_format import MessageToDict
from google.protobuf.text_format import MessageToString

class TestSuiteGrpc(unittest.TestCase):
    def setUp(self):
        self.sentences = "Ich bin das Singularität."
        self.sentences_1 = "I am the singularity. And I hope to find the best of the world. If not, as they say in french, Bye"
        self.sentences_2 = "እኔ የነጠላነት ደረጃ ነኝ::"
        self.sentences_3 = "Ich bin das Singularität. I am the singularity."
        self.sentences_4 = "Ich bin das Singularität. I am the singularity. እኔ የነጠላነት ደረጃ ነኝ:: "
        self.port = "8005"
        self.result = []

        self.server = start_service.create_server(self.port)
        self.server.start()

    def test_grpc_call(self):
        with grpc.insecure_channel('localhost:' + self.port) as channel:
            stub = LanguageDetectStub(channel)
            request = Input()
            request.input = self.sentences
            response = stub.infer(request)
            print(MessageToString(response))
            # print(MessageToDict(response))
            print(response.language[0].sentence.encode('utf-8'))
            # self.assertEqual(response, '')
            request = Input()
            request.input = self.sentences_1
            response = stub.infer(request)
            # print(MessageToDict(response))
            print(response)
            # self.assertEqual(response, '')
            request = Input()
            request.input = self.sentences_2
            response = stub.infer(request)
            # print(MessageToDict(response))
            print(response)
            # self.assertEqual(response, '')
            request = Input()
            request.input = self.sentences_3
            response = stub.infer(request)
            # print(MessageToDict(response))
            print(response)
            # self.assertEqual(response, '')
            request = Input()
            request.input = self.sentences_4
            response = stub.infer(request)
            # print(MessageToDict(response))
            print(response)

    def tearDown(self):
        self.server.stop(0)
