from abc import ABC

class Atleta(ABC):
    nome: str
    idade: int
    peso: float

    def __init__(self, n: str, i: int, p: float):
        self.nome = n
        self.idade = i
        self.peso = p

    def aquecer(self):
        return "Aquecer"
    
    def __str__(self) -> str:
        return f"Nome: {self.nome}, {self.idade} anos, {self.peso} Kg"

class Corredor(Atleta):
    
    def correr(self):
        return "Correndo"

class Nadador(Atleta):

    def nadar(self):
        return 'Nadando'

class Ciclista(Atleta):
    
    def pedalar(self):
        return 'Pedalando'