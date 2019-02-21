from service_spec.CoreferenceResolutionService_pb2 import InputSentence, ReferenceResolution, References
from service_spec.CoreferenceResolutionService_pb2_grpc import ResolveReferenceServicer, \
    add_ResolveReferenceServicer_to_server
from service.coreference_resolution import Correference_Resolver
import grpc
from concurrent import futures
import time


class ResolveReferenceServicer(ResolveReferenceServicer):
    def resolution(self, request, context):
        if request.sentence is None:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Sentence is required.")
            return ReferenceResolution()
        elif request.sentence == '':
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Sentence is empty.")
            return ReferenceResolution()

        response = ReferenceResolution()

        correference = Correference_Resolver(input_sentence=request.sentence)
        result = correference.coreference_resolution()

        for i in result.keys():
            if i == 'words':
                for j in result[i]:
                    response.words.word.append(j)
                continue

            ref = References()
            ref.key.firstIndex = i[0]
            ref.key.secondIndex = i[1]
            for values in result[i]:
                ref.mappings.add(firstIndex=values[0], secondIndex=values[1])
            response.references.add(key=ref.key, mappings=ref.mappings)

        return response


def create_server(port="50051"):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    add_ResolveReferenceServicer_to_server(ResolveReferenceServicer(), server)
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
