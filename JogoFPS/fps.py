from typing import List
from armas import *
from golpes import *

class Jogador:
    energia: float
    armas: List[Arma]

    def __init__(self):
        self.energia = 150
        self.armas: List[Arma] = []

    def add_arma(self, a: Arma):
        self.armas.append(a)

    def atirar(self, d: Disparavel, j):
        d.disparar(j)
    
    def municiar(self, d: Disparavel):
        d.recarregar()
        
    def bater(self, g: Golpe = None, a: Arma = None, j = None):
        if j == None:
            raise Exception('Bater sem parametro!')
        if g != None:
            g.golpear(j)
        elif a != None:
            a.agredir(j)

    def __str__(self):
        return f'Energia: {self.energia}'