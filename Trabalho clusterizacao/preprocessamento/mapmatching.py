from math import sqrt, pow
import sys
sys.path.append('..')
from dao.conexao import *
from dao.caminhoDAO import *
from dao.pontoDAO import *
from dao.tdrive import *
class MapMatching:
    def __init__(self, caminhoDAO, pontoDAO, tdriveDAO):
        self.caminhoDao = caminhoDAO
        self.pontoDao = pontoDAO
        self.tdriveDao = tdriveDAO
        
    def encontrar_vertice_mais_proximo(self):
        pontos = self.pontoDao.select_all()
        tdrive = self.tdriveDao.select_all()
        for row in tdrive:
            lista_distancias = []
            for ponto in pontos:
                lista_distancias.append(distancia_euclidiana(float(ponto.longitude), float(ponto.latitude), float(row[2]),float(row[3])))
        # para cada ponto, descobrir qual o vertice mais próximo

def distancia_euclidiana(x1, y1, x2, y2):
    return sqrt(pow(x1-x2, 2) + pow(y1-y2,2))

conexao = ConnectionFactory().getConection()
caminho_dao = CaminhoDAO(conexao)
ponto_dao = PontoDAO(conexao)

mapMatching = MapMatching(caminho_dao, ponto_dao)

print(mapMatching.encontrar_vertice_mais_proximo())