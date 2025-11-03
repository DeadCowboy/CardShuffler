from typing import List
from enum import Enum


class Moves(Enum):
    L = 1
    R = 2
    C = 3


class Shuffler:

    def __init__(self) -> None:
        self.leftStack = []
        self.rightStack = []
        self.mainStack = []

    def load(self, cards: List[int]) -> None:
        "Index 0 is the lowest card in the deck. Index -1 is on top"
        self.mainStack = cards

    def look(self):
        return self.mainStack[0]

    def ejectLeft(self):
        self.leftStack.append(self.mainStack.pop(0))

    def ejectRight(self):
        self.rightStack.append(self.mainStack.pop(0))

    def combineLeftFirst(self):
        self.mainStack += self.leftStack
        self.mainStack += self.rightStack
        self.leftStack = []
        self.rightStack = []

    def combineRightFirst(self):
        self.mainStack += self.rightStack
        self.mainStack += self.leftStack
        self.rightStack = []
        self.leftStack = []

    def perfMoves(self, moves: List[Moves]):
        for move in moves:
            match move:
                case Moves.L:
                    self.ejectLeft()
                case Moves.R:
                    self.ejectRight()
                case Moves.C:
                    self.combineLeftFirst()
