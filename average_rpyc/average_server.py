import time
import rpyc
from rpyc.utils.server import ThreadedServer

class Averager( rpyc.Service ):
    def exposed_avgit(self, l):
        print('Received average request [%s]' % (time.strftime('%H:%M:%S', time.gmtime())))
        a = int(round( sum(l) / len(l), 0 ))
        return a


def serve():
    t = ThreadedServer(Averager, port=50051)
    t.start()
    try:
        while True:
            time.sleep(600)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()
    