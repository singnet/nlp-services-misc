from service_spec.NamedEntityDisambiguation_pb2 import Input, Output
from service_spec.NamedEntityDisambiguation_pb2_grpc import DisambiguateStub
import unittest
import start_service
import grpc
from google.protobuf.json_format import MessageToDict

class TestSuiteGrpc(unittest.TestCase):
    def setUp(self):
        self.sentences = ["Silicon Valley is a great series. So was The Big Bang Theory.",
                          "Ryan Reynolds is a decent actor. I prefer to see Jake Gyllenhaal in movies though.",
                          "MacDonald's is great place to eat fast food.",
                          "Macdonald was a great firm before it was sold to S. J. Wolfe & Co. ", ]

        self.port = "8006"
        self.result = []

        self.server = start_service.create_server(self.port)
        self.server.start()

    def test_grpc_call(self):
        with grpc.insecure_channel('localhost:' + self.port) as channel:
            stub = DisambiguateStub(channel)
            for i in self.sentences:
                request = Input()
                request.input = i
                response = stub.named_entity_disambiguation(request)
                print(MessageToDict(response))
                print(response)

    def tearDown(self):
        self.server.stop(0)
