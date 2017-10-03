import sys
sys.path.append("..") # "Sobe" uma pasta para que seja possível importar o model.vertice.Vertice
from model.vertice import *

class vertice_Dao:
    def __init__(self):
        pass
    def file_to_vert_list(self, file):
        lista = []
        for line in open(file):
            linha = line.split(',')
            vertice = Vertice(linha[0], linha[1], linha[2], linha[3])
            lista.append(vertice)
        return lista

dao = vertice_Dao()
lista_ = dao.file_to_vert_list("../1.txt")
print(lista_[0].get_latitude())