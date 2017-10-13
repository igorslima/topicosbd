from conexao import ConnectionFactory
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
    def __init__(self, cursor):
        self.cursor = cursor
        
    def file_to_vert_list(self, file):
        lista = []
        arquivo = open(file)
        for line in arquivo:
            linha = line.split(',')
            vertice = [linha[0], linha[1], linha[2], linha[3]]
            lista.append(vertice)
        arquivo.close()
        return lista

    def salvar_into_db(self):
        lista_arquivos = os.listdir("../taxi_log_2008_by_id/")
        qtd_arquivos = len(lista_arquivos)
        qtd_linhas = 0
        qtd_arquivos_lidos = 0
        for arquivo in lista_arquivos:
            lista = self.file_to_vert_list('../taxi_log_2008_by_id/{}'.format(arquivo))
            cont_arquivo = 0
            for item in lista:
                self.cursor.execute("INSERT INTO public.vertices(id_taxista, date_time, longitude, latitude) VALUES (%s, %s, %s, %s)",[lista[cont_arquivo][0],lista[cont_arquivo][1], lista[cont_arquivo][2], lista[cont_arquivo][3]])
                cont_arquivo += 1
                qtd_linhas += 1
            print("O contador de arquivo está em: {}".format(cont_arquivo))
            print("A quantidade de linhas está em: {}".format(qtd_linhas))
            qtd_arquivos_lidos += 1
            print("% de arq lidos: {}".format(qtd_arquivos_lidos/qtd_arquivos * 100))
        print("O contado de linhas terminou em {}:".format(qtd_linhas))
connectionFactory = ConnectionFactory()
con = connectionFactory.getConection()
cursor = con.cursor()
dao = vertice_Dao(cursor)
#lista_ = dao.file_to_vert_list("../1.txt")
dao.salvar_into_db()
con.commit()
cursor.close()
con.close()