from typing import List
from enum import Enum
import math


class Moves(Enum):
    L = 1
    R = 2
    C = 3
    CL = 4
    CR = 5


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

    def lookLeft(self):
        return self.leftStack[0] if len(self.leftStack) > 0 else math.inf

    def lookRight(self):
        return self.rightStack[0] if len(self.rightStack) > 0 else math.inf

    def ejectLeft(self):
        self.leftStack.append(self.mainStack.pop(0))

    def ejectRight(self):
        self.rightStack.append(self.mainStack.pop(0))

    def leftToMain(self):
        self.mainStack.append(self.leftStack.pop(0))

    def rightToMain(self):
        self.mainStack.append(self.rightStack.pop(0))

    def perfMoves(self, moves: List[Moves]):
        for move in moves:
            match move:
                case Moves.L:
                    self.ejectLeft()
                case Moves.R:
                    self.ejectRight()
                case Moves.CL:
                    self.leftToMain()
                case Moves.CR:
                    self.rightToMain()
