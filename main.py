import random
from Shuffler import Shuffler, Moves
import copy
import math


shuffler = Shuffler()
trueNumCards = 6
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


interval = numCards

while interval > 1:
    for i in range(numCards // interval):
        sortSegment(interval, interval * i + interval // 2)
        shuffler.combineLeftFirst()
        moves.append(Moves.C)

    interval = interval // 2

# Tests
print("### Test ###")
testShuffler = Shuffler()
testShuffler.load(realCardDeck)
testShuffler.perfMoves(moves)
# print(moves)
print(f"value: {sum([1 for x in moves if x == Moves.C])}")
print(testShuffler.mainStack)
