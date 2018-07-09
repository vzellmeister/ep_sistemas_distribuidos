import grpc
from concurrent import futures
import time

# import the generated classes
import void_pb2
import void_pb2_grpc

class DoerServicer(void_pb2_grpc.DoerServicer):

    def DoSomething(self, request, context):
        '''There is only the void'''
        return void_pb2.Empty()

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
void_pb2_grpc.add_DoerServicer_to_server(
        DoerServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)