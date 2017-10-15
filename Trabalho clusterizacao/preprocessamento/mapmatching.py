from math import sqrt
import sys
sys.path.append('..')
from dao.conexao import *
from dao.caminhoDAO import *
from dao.pontoDAO import *
from dao.tdrive import *
from dao.HashMapDAO import *
class MapMatching:
    def __init__(self, caminhoDAO, pontoDAO, tdriveDAO, hashMapDAO):
        self.caminhoDao = caminhoDAO
        self.pontoDao = pontoDAO
        self.tdriveDao = tdriveDAO
        self.hashMaoDao = hashMapDAO
        
    def encontrar_vertice_mais_proximo(self):
        pontos = self.pontoDao.select_all()
        tdrive = self.tdriveDao.select_all()
        cont = 0
        for row in tdrive:
            menor_distancia = sys.maxsize
            ponto_mais_proximo = None 
            for ponto in pontos:
                dist = distancia_euclidiana(float(ponto.longitude), float(ponto.latitude), float(row[3]),float(row[4]))
                if(dist < menor_distancia):
                    ponto_mais_proximo = ponto
                    menor_distancia = dist
            print("O ponto mais proximo é {}".format(menor_distancia))
            self.hashMaoDao.inserir_no_banco(ponto_mais_proximo.id, row[0])
            print("A qtd está em {}".format((cont/17662983) * 100))
            cont += 1
        del(tdrive)
        del(pontos)
    def update_row_tdrive(self, linha, nova_posicao):
        self.tdriveDao.update_row(linha, nova_posicao)
def distancia_euclidiana(x1, y1, x2, y2):
    return sqrt(pow(x1-x2, 2) + pow(y1-y2,2))

conexao = ConnectionFactory().getConection()
caminho_dao = CaminhoDAO(conexao)
ponto_dao = PontoDAO(conexao)
tdrive_dao = TdriveDAO(conexao)
hashMap_dao = HashMapDAO(conexao)
mapMatching = MapMatching(caminho_dao, ponto_dao, tdrive_dao, hashMap_dao)
print(mapMatching.encontrar_vertice_mais_proximo())
conexao.close()