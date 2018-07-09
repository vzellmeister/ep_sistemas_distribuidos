import grpc
from concurrent import futures
import time

# import the generated classes
import analyzer_pb2
import analyzer_pb2_grpc

class AnalyzerServicer(analyzer_pb2_grpc.AnalyzerServicer):

    # analyzer.score : calculate user score
    def score(self, request, context):
        print('Received sort request [%s]' % (time.strftime('%H:%M:%S', time.gmtime())))

        data = request
        sc = data.level.bonus
        for i in range(0, len(data.plays)):
            play = data.plays[i]
            sc += (2.5 - play.time) * 2 * data.level.multiplier * play.precision

        response = analyzer_pb2.Score()
        response.score = int(sc)
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
analyzer_pb2_grpc.add_AnalyzerServicer_to_server(
        AnalyzerServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)