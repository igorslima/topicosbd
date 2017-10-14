from math import sqrt, pow
import sys
sys.path.append('..')
from dao.conexao import *
from dao.caminhoDAO import *
from dao.pontoDAO import *

class MapMatching:
    def __init__(self, caminhoDAO, pontoDAO):
        self.caminhoDao = caminhoDAO
        self.pontoDao = pontoDAO
        
    def encontrar_vertice_mais_proximo(self):
        caminhos = self.caminhoDao.select_all()
        pontos = self.pontoDao.select_all()
        for aresta in caminhos:
            print(aresta.id)
        # para cada ponto, descobrir qual o vertice mais próximo

def distancia_euclidiana(x1, y1, x2, y2):
    return sqrt(pow(x1-x2, 2) + pow(y1-y2,2))

conexao = ConnectionFactory().getConection()
caminho_dao = CaminhoDAO(conexao)
ponto_dao = PontoDAO(conexao)

mapMatching = MapMatching(caminho_dao, ponto_dao)

print(mapMatching.encontrar_vertice_mais_proximo())