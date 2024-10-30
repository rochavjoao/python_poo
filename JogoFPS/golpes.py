from abc import ABC, abstractmethod
from fps import *

class Golpe(ABC):
    @abstractmethod
    def golpear(self, j: Jogador):
        pass


class Soco(Golpe):
    def golpear(self, j: Jogador):
        j.energia -= 1


class Chute(Golpe):
    def golpear(self, j: Jogador):
        j.energia -= 2