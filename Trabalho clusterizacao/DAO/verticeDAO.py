import sys
sys.path.append("..") # "Sobe" uma pasta para que seja possível importar o model.vertice.Vertice

#para saber o caminho do arquivo
#import os 
#dir_path = os.path.dirname(os.path.realpath(__file__))
#print(dir_path)

from model.vertice import *
import pandas as pd
import os
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
    def join_all_files(self):
        df = pd.DataFrame()
        df['id_taxista'] = 0
        df['date_time'] = 0
        df['longitude'] = 0
        df['latitude'] = 0
        lista_arquivos = os.listdir("../taxi_log_2008_by_id/")
        cont = 0
        for arquivo in lista_arquivos:
            lista = self.file_to_vert_list('../taxi_log_2008_by_id/{}'.format(arquivo))
            print(cont)
            cont += 1
        return df
        #return df
dao = vertice_Dao()
#lista_ = dao.file_to_vert_list("../1.txt")
dao.join_all_files()