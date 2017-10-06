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
            vertice = [375082,linha[0], linha[1], linha[2], linha[3]]
            lista.append(vertice)
        #close(file) TODO função fechar python
        return lista
    def join_all_files_into_a_data_set(self):
        df = pd.DataFrame()
        df['matricula'] = 375082
        df['id_taxista'] = 0
        df['date_time'] = 0
        df['longitude'] = 0
        df['latitude'] = 0
        lista_arquivos = os.listdir("../taxi_log_2008_by_id//")
        qtd_arquivos = len(lista_arquivos)
        qtd_linhas = 0
        qtd_arquivos_lidos = 0
        for arquivo in lista_arquivos:
            lista = self.file_to_vert_list('../taxi_log_2008_by_id/{}'.format(arquivo))
            cont_arquivo = 0
            for item in lista:
                df.loc[qtd_linhas] = lista[cont_arquivo]
                cont_arquivo += 1
                qtd_linhas += 1
            print("O contador de arquivo está em: {}".format(cont_arquivo))
            print("A quantidade de linhas está em: {}".format(qtd_linhas))
            qtd_arquivos_lidos += 1
            print("% de arq lidos: {}".format(qtd_arquivos_lidos/qtd_arquivos * 100) )
        print("O contado de linhas terminou em {}:".format(qtd_linhas))
        
        return df
        #return df
dao = vertice_Dao()
#lista_ = dao.file_to_vert_list("../1.txt")
dados = dao.join_all_files_into_a_data_set()
print(dados)