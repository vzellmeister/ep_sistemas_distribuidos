import time
import rpyc
from rpyc.utils.server import ThreadedServer

class Formatter( rpyc.Service ):

    # Makes all characters in string upper case
    def exposed_Upper(self, _str):
        print('Upper request received at: %s' % (time.strftime('%H:%M:%S', time.gmtime())))
        return _str.upper()

    # Makes all characters in string lower case
    def exposed_Lower(self, _str):
        print('Lower request received at: %s' % (time.strftime('%H:%M:%S', time.gmtime())))
        return _str.lower()

    # Makes first character in each word upper case, all other characters lower case
    def exposed_Proper(self, _str):
        print('Proper request received at: %s' % (time.strftime('%H:%M:%S', time.gmtime())))
        return _str.title()

def serve():
    t = ThreadedServer(Formatter, port=50051)
    t.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()