import grpc
from concurrent import futures
import time

# import the generated classes
import average_pb2
import average_pb2_grpc

class AveragerServicer(average_pb2_grpc.AveragerServicer):

    # calculator.square_root is exposed here
    # the request and response are of the data type
    # calculator_pb2.Number
    def avgit(self, request, context):
        print('Received sort request [%s]' % (time.strftime('%H:%M:%S', time.gmtime())))
        l = request.values
        l.sort()
        response = average_pb2.avg()
        response.num = int(round( sum(l) / len(l), 0 ))
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
average_pb2_grpc.add_AveragerServicer_to_server(
        AveragerServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)