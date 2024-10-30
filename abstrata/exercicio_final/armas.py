from abc import ABC, ABCMeta, abstractmethod
from fps import *
from golpes import *

class Arma(ABC):
    destruicao: float

    def __init__(self, d: float):
        self.destruicao = d

    def agredir(self, j: Jogador):
        j.energia -= 5

    def __str__(self):
        return f'Poder de destruição: {self.destruicao}'

class Faca(Arma):
    lamina: int

    def __init__(self):
        self.destruicao = 15
        self.lamina = 10

    def agredir(self, j: Jogador):
        self.lamina -= 1
        if self.lamina > 0:
            j.energia -= self.destruicao
        else:
            super().agredir(j)

class Disparavel(metaclass=ABCMeta):
    @abstractmethod
    def disparar(self, j: Jogador):
        pass
    
    @abstractmethod
    def recarregar(self):
        pass

class Revolver(Arma, Disparavel):
    cartuchos: int

    def __init__(self):
        self.destruicao = 20
        self.cartuchos = 6
    
    def disparar(self, j: Jogador):
        if self.cartuchos > 0:
            self.cartuchos -= 1
            j.energia -= self.destruicao
        else:
            self.agredir(j)
    
    def recarregar(self):
        self.cartuchos = 6

class Lanca_Chamas(Arma, Disparavel):
    gas: float

    def __init__(self):
        self.destruicao = 30
        self.gas = 100

    def disparar(self, j: Jogador):
        if self.gas > 0:
            self.gas -= 5.5
            j.energia -= self.destruicao
    
    def recarregar(self):
        self.gas = 100

class Soco_Ingles(Faca, Soco):
    def agredir(self, j: Jogador):
        super().agredir(j)
        self.golpear(j)
    