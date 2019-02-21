from service.named_entity_disambiguation import NamedEntityDisambiguation
from service_spec.NamedEntityDisambiguation_pb2 import Input, Output, Disambiguation
from service_spec.NamedEntityDisambiguation_pb2_grpc import add_DisambiguateServicer_to_server, DisambiguateServicer
import grpc
from concurrent import futures
import time


class DisambiguateServicer(DisambiguateServicer):
    def __init__(self):
        self.disambiguate = NamedEntityDisambiguation()

    def named_entity_disambiguation(self, request, context):
        if request.input is None:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Sentence is required.")
            return Output()
        elif request.input == '':
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Sentence is empty.")
            return Output()

        response = Output()

        named_entities, candidates = self.disambiguate.named_entity_disambiguation(request.input)

        if not named_entities:
            disambiguation = response.disambiguation.add()
            return response

        if not candidates:
            disambiguation = response.disambiguation.add()
            return response

        for named, candidate in zip(named_entities, candidates):
            disambiguation = response.disambiguation.add()
            disambiguation.named_entity = named
            if candidate is not None:
                disambiguation.disambiguation_word = candidate[0]
                disambiguation.disambiguation_link = candidate[1]

        return response


def create_server(port="50051"):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    add_DisambiguateServicer_to_server(DisambiguateServicer(), server)
    server.add_insecure_port('[::]:' + str(port))
    return server


if __name__ == '__main__':
    server = create_server()
    server.start()
    _ONE_DAY = 60 * 60 * 24
    try:
        while True:
            time.sleep(_ONE_DAY)
    except KeyboardInterrupt:
        server.stop(0)
