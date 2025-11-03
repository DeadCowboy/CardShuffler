import random
from Shuffler import Shuffler, Moves
import copy
import math

shuffler = Shuffler()
trueNumCards = 52
numCards = 2 ** math.ceil(math.log2(trueNumCards))
realCardDeck = list(range(trueNumCards))
random.seed(1)
random.shuffle(realCardDeck)
cardDeck = realCardDeck + list(range(trueNumCards, numCards))
shuffler.load(cardDeck)
moves = []

print(cardDeck)


def sortSegment(length: int, pivot: int):
    for i in range(length):
        if (val := shuffler.look()) < pivot:
            shuffler.ejectLeft()
            if val < trueNumCards:
                moves.append(Moves.L)
        else:
            shuffler.ejectRight()
            if val < trueNumCards:
                moves.append(Moves.R)


# Size of one block to be sorted
interval = numCards

while interval > 1:
    for i in range(numCards // interval):
        sortSegment(interval, interval * i + interval // 2)

    # Virtual shuffle
    for i in range(numCards // interval):
        for l in range(interval // 2):
            if shuffler.lookLeft() < trueNumCards:
                moves.append(Moves.CL)
            shuffler.leftToMain()
        for r in range(interval // 2):
            if shuffler.lookRight() < trueNumCards:
                moves.append(Moves.CR)
            shuffler.rightToMain()

    interval = interval // 2


# Tests
print("### Test ###")
testShuffler = Shuffler()
testShuffler.load(realCardDeck)
testShuffler.perfMoves(moves)
print(testShuffler.mainStack)
