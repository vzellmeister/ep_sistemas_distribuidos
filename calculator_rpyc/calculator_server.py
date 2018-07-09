import time
import rpyc
from rpyc.utils.server import ThreadedServer

class Calculator( rpyc.Service ):

    def exposed_Addition(self, a, b):
        print('Received Addition request [%s]' % (time.strftime('%H:%M:%S', time.gmtime())))
        return a + b

    def exposed_Subtraction(self, a, b):
        print('Received Subtraction request [%s]' % (time.strftime('%H:%M:%S', time.gmtime())))
        return a - b

    def exposed_Multiplication(self, a, b):
        print('Received Multiplication request [%s]' % (time.strftime('%H:%M:%S', time.gmtime())))
        return a * b
    
    def exposed_Division(self, a, b):
        print('Received Division request [%s]' % (time.strftime('%H:%M:%S', time.gmtime())))
        return a / b

def serve():
    t = ThreadedServer(Calculator, port=50051)
    t.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()
    