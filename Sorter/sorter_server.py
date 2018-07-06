from concurrent import futures
import time

import grpc

import pickle
import sorter_pb2
import sorter_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Sorter(sorter_pb2_grpc.StringFormatterServicer):

    def sort(self, request, context):
        print('Received Sort request [%s]' % (time.strftime('%H:%M:%S', time.gmtime())))
        return sorter_pb2.sortReply( pickle.dumps( pickle.loads( sortRep=request.sortReq ).sort() ) )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sorter_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()