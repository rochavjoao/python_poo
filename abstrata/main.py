from atletas import *

if __name__ == "__main__":

    c1 = Corredor('Bolt', 34, 90.5)
    n1 = Nadador('Cesar Cielo', 42, 85.5)
    cicl1 = Ciclista('Neymar', 32, 74.3)
    tri = Triatleta('Fernanda Keller', 42, 65.3)

    print(c1)
    print(c1.aquecer())
    print(c1.correr())
    print(n1)
    print(n1.aquecer())
    print(n1.nadar())
    print(cicl1)
    print(cicl1.aquecer())
    print(cicl1.pedalar())

    print(tri)
    print(tri.realizar_maratona())
    print(Triatleta.__mro__)