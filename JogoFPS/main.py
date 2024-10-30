from golpes import *
from fps import Jogador
from armas import *

if __name__ == '__main__':
    j1 = Jogador()
    j2 = Jogador()
    print(f'Jogador 1 {j1}')
    print(f'Jogador 2 {j2}')
    
    j1.bater(a=Revolver(), j=j2)

    print(f'Jogador 1 {j1}')
    print(f'Jogador 2 {j2}')