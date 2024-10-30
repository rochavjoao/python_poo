from golpes import *
from fps import *
from armas import *

if __name__ == '__main__':
    j1 = Jogador()
    print(f'Jogador 1 {j1}')
    si = Soco_Ingles()

    print(j1)
    for x in range(1,11):
        print(x)
        si.agredir(j1)
        print(j1)