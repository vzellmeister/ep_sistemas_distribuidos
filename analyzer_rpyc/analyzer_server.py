import time
import pickle
import rpyc
from rpyc.utils.server import ThreadedServer


# Data structures definitions
class Data():
    def __init__(self, id, username, level, plays = []):
        self.id = id
        self.username = username
        self.level = level
        self.plays = plays

class Level():
    def __init__(self, bonus, multiplier):
        self.bonus = bonus
        self.multiplier = multiplier

class Play():
    def __init__(self, time, precision):
        self.time = time
        self.precision = precision


# Analyzer service
class Analyzer( rpyc.Service ):
    def exposed_score(self, slz):
        print('Received sort request [%s]' % (time.strftime('%H:%M:%S', time.gmtime())))
        
        data = pickle.loads(slz)
        sc = data.level.bonus
        for i in range(0, len(data.plays)):
            play = data.plays[i]
            sc += (2.5 - play.time) * 2 * data.level.multiplier * play.precision
        return int(sc)


def serve():
    t = ThreadedServer(Analyzer, port=50051)
    t.start()
    try:
        while True:
            time.sleep(600)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()
    