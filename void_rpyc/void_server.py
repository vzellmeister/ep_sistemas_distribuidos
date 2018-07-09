import time
import rpyc
from rpyc.utils.server import ThreadedServer

class Doer( rpyc.Service ):
    '''There is only the void'''
    def exposed_doSomething(self):
        return None # Returns nothing


def serve():
    t = ThreadedServer(Doer, port=50051)
    t.start()
    while True:
        time.sleep(600)


if __name__ == "__main__":
    serve()
    