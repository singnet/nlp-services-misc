from service.language_detection import LanguageDetector
from service_spec.LanguageDetection_pb2 import Input, Output, Prediction, Language
from service_spec.LanguageDetection_pb2_grpc import LanguageDetectServicer, add_LanguageDetectServicer_to_server
import grpc
from concurrent import futures
import time


class LanguageDetectServicer(LanguageDetectServicer):
    def infer(self, request, context):
        if request.input is None:
            raise InvalidParams("Invalid Sentence")
        elif request.input == '':
            raise InvalidParams("Empty Sentence")

        response = Output()

        detector = LanguageDetector()

        result = detector.language_id(request.input)

        for key, value in result.items():
            lang = response.language.add()
            lang.sentence = key
            for k, v in value.items():
                pred = lang.prediction.add()
                pred.language = k
                pred.confidence = v

        return response


def create_server(port="8001"):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    add_LanguageDetectServicer_to_server(LanguageDetectServicer(), server)
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
