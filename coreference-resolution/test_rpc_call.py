from service_spec.CoreferenceResolutionService_pb2 import InputSentence, ReferenceResolution
from service_spec.CoreferenceResolutionService_pb2_grpc import ResolveReferenceServicer, \
    add_ResolveReferenceServicer_to_server, ResolveReferenceStub
import unittest
import start_service
import grpc
from google.protobuf.json_format import MessageToJson, MessageToDict


class TestSuiteGrpc(unittest.TestCase):
    def setUp(self):
        self.sentences = [
            "Michael is a great man. He does what is required of him.",
            "Paul Allen Tohmas was born on January 21, 1953, in Seattle, Washington, to Kenneth Sam Allen and Edna Faye Allen. Allen attended Lakeside School, a private school in Seattle, where he befriended Bill Gates, two years younger, with whom he shared an enthusiasm for computers. Paul and Bill used a teletype terminal at their high school, Lakeside, to develop their programming skills on several time-sharing computer systems."]
        # self.sentences = ["Michael is a great man. He does what is required of him."]
        self.expected_result = [{'references': [{'key': {'firstIndex': 0, 'secondIndex': 0},
                                                 'mappings': [{'firstIndex': 6, 'secondIndex': 6},
                                                              {'firstIndex': 12, 'secondIndex': 12}]}], 'words': {
            'word': ['Michael', 'is', 'a', 'great', 'man', '.', 'He', 'does', 'what', 'is', 'required', 'of', 'him',
                     '.']}}, {'references': [{'key': {'secondIndex': 2, 'firstIndex': 0},
                                              'mappings': [{'firstIndex': 21, 'secondIndex': 23},
                                                           {'firstIndex': 25, 'secondIndex': 25},
                                                           {'firstIndex': 37, 'secondIndex': 37},
                                                           {'firstIndex': 48, 'secondIndex': 48}]},
                                             {'key': {'firstIndex': 12, 'secondIndex': 12},
                                              'mappings': [{'firstIndex': 34, 'secondIndex': 34}]},
                                             {'key': {'firstIndex': 39, 'secondIndex': 40},
                                              'mappings': [{'firstIndex': 57, 'secondIndex': 57}]},
                                             {'key': {'firstIndex': 55, 'secondIndex': 57},
                                              'mappings': [{'firstIndex': 63, 'secondIndex': 63},
                                                           {'firstIndex': 71, 'secondIndex': 71}]}], 'words': {
            'word': ['Paul', 'Allen', 'Tohmas', 'was', 'born', 'on', 'January', '21', ',', '1953', ',', 'in', 'Seattle',
                     ',', 'Washington', ',', 'to', 'Kenneth', 'Sam', 'Allen', 'and', 'Edna', 'Faye', 'Allen', '.',
                     'Allen', 'attended', 'Lakeside', 'School', ',', 'a', 'private', 'school', 'in', 'Seattle', ',',
                     'where', 'he', 'befriended', 'Bill', 'Gates', ',', 'two', 'years', 'younger', ',', 'with', 'whom',
                     'he', 'shared', 'an', 'enthusiasm', 'for', 'computers', '.', 'Paul', 'and', 'Bill', 'used', 'a',
                     'teletype', 'terminal', 'at', 'their', 'high', 'school', ',', 'Lakeside', ',', 'to', 'develop',
                     'their', 'programming', 'skills', 'on', 'several', 'time', '-', 'sharing', 'computer', 'systems',
                     '.']}}]

        self.port = "8001"
        self.result = []

        self.server = start_service.create_server(self.port)
        self.server.start()

    def test_grpc_call(self):
        with grpc.insecure_channel('localhost:' + self.port) as channel:
            stub = ResolveReferenceStub(channel)
            for i in self.sentences:
                request = InputSentence(sentence=i)
                response = stub.resolution(request)
                print(response)
                self.result.append(MessageToDict(response, including_default_value_fields=True))
            self.assertMultiLineEqual(str(self.result), str(self.expected_result))

    def tearDown(self):
        self.server.stop(0)
