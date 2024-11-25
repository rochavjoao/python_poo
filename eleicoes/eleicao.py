import pickle
from typing import List
from common import *
from datetime import date
from int_grafica import *

class Urna(Transparencia):
    mesario : Pessoa
    __secao : int
    __zona : int
    __eleitores_presentes : List[Eleitor] = []
    __votos = {} #dicionario chave = numero do candidato, valor é a quantidade de votos

    def __init__(self, mesario : Pessoa, secao : int, zona : int,
                 candidatos : List[Candidato], eleitores : List[Eleitor]):
        self.mesario = mesario
        self.__secao = secao
        self.__zona = zona
        self.__nome_arquivo = f'{self.__zona}_{self.__secao}.pkl'
        self.__candidatos = candidatos
        self.__eleitores = []
        for eleitor in eleitores:
            if eleitor.zona == zona and eleitor.secao == secao:
                self.__eleitores.append(eleitor)

        for candidato in self.__candidatos:
            self.__votos[candidato.get_numero()] = 0
        self.__votos['BRANCO'] = 0
        self.__votos['NULO'] = 0

        with open(self.__nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)

    def get_eleitor(self, titulo : int):
        for eleitor in self.__eleitores:
            if eleitor.get_titulo() == titulo:
                return eleitor
        return False

    def registrar_voto(self, eleitor : Eleitor, n_cand : int):
        self.__eleitores_presentes.append(eleitor)
        if n_cand in self.__votos:
            self.__votos[n_cand] += 1
        elif n_cand == 0:
            self.__votos['BRANCO'] += 1
        else:
            self.__votos['NULO'] += 1

        with open(self.__nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)

    def __str__(self):
        data_atual = date.today()#from datalime import date
        info = (f'Urna da seção {self.__secao}, zona {self.__zona}\n'
                f'Mesario {self.mesario}\n')
        info += f'{data_atual.ctime()}\n'

        for k, v in self.__votos.items():
            info += f'Candidato {k} = {v} votos\n'

        return info

    def zerisima(self):
        with open('zerisima' +self.__nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)

    def encerrar(self):
        with open('final_'+self.__nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)