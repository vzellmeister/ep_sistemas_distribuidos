import rpyc
import time
import random
import pickle


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


# Generate random data
def create_data():
    lvl = Level( random.randint(100,1000), random.uniform(1, 1.75) )
    plays = []
    for e in range(0,100):
        plays.append( Play( random.uniform(0.2, 3.5), random.uniform(.6,.98) ) )
    data = Data( random.randint(1,10), "Username", lvl, plays )
    return data



# Client code
def run():
    # Create RPyC connection
    conn = rpyc.connect("localhost", 50051, config={'allow_all_attrs':True})

    print("Generating data...")
    data = create_data()
    slz = pickle.dumps(data)

    print("Calling server...")
    tm_start = time.time()
    score = conn.root.score(slz)
    tm_end = time.time()
    print('Score %d [%s]' % (score, tm_end - tm_start))


if __name__ == '__main__':
    run()
