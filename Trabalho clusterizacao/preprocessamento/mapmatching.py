from math import sqrt, pow
import sys
sys.path.append('..')
from dao.conexao import *
from dao.caminhoDAO import *
from model.vertice import *
class MapMatching:
    def __init__(self, caminhoDAO):
        self.caminhoDao = caminhoDAO
        
    def encontrar_vertice_mais_proximo(self):
        lista = self.caminhoDao.select_all()
        return None

def distancia_euclidiana(x1, y1, x2, y2):
    return sqrt(pow(x1-x2, 2) + pow(y1-y2,2))

print(distancia_euclidiana(4,4,3,3))
#conexao = ConnectionFactory().getConection()