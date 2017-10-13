from conexao import ConnectionFactory
import sys
sys.path.append("..")
from model.ponto import * 
class PontoDAO:
    def __init__(self, conexao):
        self.conexao = conexao
        
    def read_csv_to_db(self):
        cursor = conexao.cursor()
        pontos = open("../arquivos/table_vertices.csv")
        for p in pontos:
            linha = p.split(';')
            self.cursor.execute("INSERT INTO public.pontos (id_ponto, longitude, latitude) values (%s, %s, %s)",[linha[0], linha[1], linha[2]])
        pontos.close()
        conexao.commit()
        cursor.close()

    def select_all(self):
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM pontos;")
        resultado = cursor.fetchall()
        lista = []
        for r in resultado:
            ponto = Ponto(r[0], r[1], r[2])
            lista.append(ponto)
        print(resultado[0])
        cursor.close()
        return lista


connectionFactory = ConnectionFactory()
conexao = connectionFactory.getConection()
cursor = conexao.cursor()
dao = PontoDAO(cursor)
dao.select_all()
conexao.commit()
cursor.close()
conexao.close()