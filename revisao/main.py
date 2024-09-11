from quiz import *
if __name__ == '__main__':
    q1 = Quiz('POO', 'Joao', 10, 2)
    q2 = Quiz2A('POO', 'Vitor', 5, 7)
    q3 = Quiz3A('POO', 'Biel', 11, 1)

    print(q1)
    print(q2)
    print(q3)

    print('Testando metodos separados')
    print(q1.get_acertos())
    print(q1.get_erros())
    print(q1.calcular_pontos())