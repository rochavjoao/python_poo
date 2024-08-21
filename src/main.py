from frota import *

def operar_carro(carro : Carro):
    print('1- Ligar motor')
    print('2- Desligar motor')
    print('3- Acelerar')

    op = 0
    while op not in (1, 2, 3):
        op = int(input("Digite as opcoes[1-3]: "))

    if op == 1:
        carro.ligar()
    elif op == 2:
        carro.desligar()
    elif op == 3:
        v = float(input("Informe a velocidade: "))
        t = float(input("Informe o tempo: "))
        carro.acelerar(v, t)

    print('Infos atuais do carro')
    print(carro)
    print()

if __name__ == "__main__":
    print('Cadastre o primeiro carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, 0, False)

    print('Cadastre o segundo carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')

    carro2 = Carro(nm_modelo, nm_marca, nm_cor, 0, False)

    '''
    Controlando 2 carros até ele atingir 600 Km
    '''
    while carro1.odometro < 600 and carro2.odometro < 600:
        try:
            x = 0
            while x not in (1, 2):
                x = int(input("Qual carro voce quer operar? [1-2]: "))

            if x == 1:
                operar_carro(carro1)
            else:
                operar_carro(carro2)

        except Exception as e:
            print("Erro!")
            print(e)

carro1.desligar()
carro2.desligar()
print(carro1)
print("\n")
print(carro2)

if carro1.odometro > carro2.odometro:
    print(f"\nO {carro1.modelo} chegou primeiro")
else:
    print(f"\nO {carro2.modelo} chegou primeiro")