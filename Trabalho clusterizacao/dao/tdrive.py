import psycopg2
from conexao import *
class tdrivedao():
    def __init__(self, conexao):
        self.conexao = conexao
    
    def get_all(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM tdrive WHERE SUBSTRING(datetime, 12,2) = '04' OR SUBSTRING(datetime, 12,2) = '01' OR SUBSTRING(datetime, 12,2) = '23';")
        resultado = cursor.fetchall() #4567891011 12:04:55
        for row in resultado:
            print(row)
        cursor.close()
        #print(len(resultado))
    def salvar_tdrive_no_banco(self):
        arquivo = open('../arquivos/tdrive.csv')
        cursor = self.conexao.cursor()
        cont = 0
        for linha in arquivo:
            linha = linha.split(';')
            cursor.execute("INSERT INTO tdrive (taxista_id, datetime, longitude, latitude) values (%s, %s, %s, %s);",[linha[0], linha[1], linha[2], linha[3]])
            cont += 1
            print("A qtd está em {}".format((cont/17662983) * 100))
        arquivo.close()
        self.conexao.commit()
        cursor.close()
# conexao = ConnectionFactory().getConection()
# tdrive = tdrivedao(conexao)
# tdrive.get_all()
# conexao.close()