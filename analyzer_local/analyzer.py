import random

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


class Analyzer():
    def score(self, data):
        sc = data.level.bonus
        for i in range(0, len(data.plays)):
            play = data.plays[i]
            sc += (2.5 - play.time) * 2 * data.level.multiplier * play.precision
        return int(sc)


def create_data():
    lvl = Level( random.randint(100,1000), random.uniform(1, 1.75) )
    plays = []
    for e in range(0,100):
        plays.append( Play( random.uniform(0.2, 3.5), random.uniform(.6,.98) ) )
    data = Data( random.randint(1,10), "Username", lvl, plays )
    return data

data = create_data()
ann = Analyzer()
score = ann.score( data )
print(score)