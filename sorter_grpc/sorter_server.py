import grpc
from concurrent import futures
import time

# import the generated classes
import sorter_pb2
import sorter_pb2_grpc

class SorterServicer(sorter_pb2_grpc.SorterServicer):

    # calculator.square_root is exposed here
    # the request and response are of the data type
    # calculator_pb2.Number
    def sortit(self, request, context):
        print('Received sort request [%s]' % (time.strftime('%H:%M:%S', time.gmtime())))
        l = request.values
        l.sort()
        response = sorter_pb2.List()
        response.values.extend(l)
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
sorter_pb2_grpc.add_SorterServicer_to_server(
        SorterServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)