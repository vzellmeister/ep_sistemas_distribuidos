import time
import rpyc
from rpyc.utils.server import ThreadedServer

class Sorter( rpyc.Service ):
    def exposed_sortit(self, l):
        print('Received sort request [%s]' % (time.strftime('%H:%M:%S', time.gmtime())))
        l.sort()
        return l


def serve():
    t = ThreadedServer(Sorter, port=50051)
    t.start()
    try:
        while True:
            time.sleep(600)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()
    