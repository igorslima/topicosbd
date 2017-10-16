from math import sqrt
import sys
sys.path.append('..')
from dao.conexao import *
from dao.caminhoDAO import *
from dao.pontoDAO import *
from dao.tdrive import *
from dao.HashMapDAO import *
from operator import itemgetter
class MapMatching:
    def __init__(self, caminhoDAO, pontoDAO, tdriveDAO, hashMapDAO):
        self.caminhoDao = caminhoDAO
        self.pontoDao = pontoDAO
        self.tdriveDao = tdriveDAO
        self.hashMapDao = hashMapDAO
        
    def encontrar_vertice_mais_proximo(self):
        pontos = self.pontoDao.select_all()
        tdrive = self.tdriveDao.select_all()
        lista = []
        cont = 0
        for row in tdrive:
            menor_distancia = sys.maxsize
            ponto_mais_proximo = None
            tupla = ()
            lista_menores = []
            for ponto in pontos:
                dist = distancia_euclidiana(float(ponto.longitude), float(ponto.latitude), float(row[3]),float(row[4]))
                if(dist < menor_distancia):
                    ponto_mais_proximo = ponto
                    menor_distancia = dist
                    tupla = (row[0], ponto_mais_proximo.id, dist)
                    lista_menores.append(tupla)
            lista_menores = sorted(lista_menores, key=itemgetter(1))
            lista.append(lista_menores[0])
            lista_menores.clear()
            cont += 1
            print("Calculei a distância de {}".format(cont))
        print("Vou salvar todos no banco")
        cont = 0
        for item in lista:
            self.hashMapDao.inserir_no_banco(item[0], item[1])
            cont += 1
            print("Salvei {} no banco".format(cont))
        print("Salvei todos no banco")
        tdrive.clear()
        ponto.clear()
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