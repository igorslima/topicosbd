"""
Modulo de Dao para o tdrive
"""
#from conexao import *
class TdriveDAO():
    """
    Classe de Dao para o tdrive
    """
    def __init__(self, conexao):
        self.conexao = conexao
    def select_all(self):
        """
        Seleciona todos as colunas do banco com das horas 04, 01 e 23

        """
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM tdrive WHERE SUBSTRING(datetime, 12,2) = '04' OR SUBSTRING(datetime, 12,2) = '01' OR SUBSTRING(datetime, 12,2) = '23';")
        resultado = cursor.fetchall() #4567891011 12:04:55
        cursor.close()
        return resultado
    def salvar_tdrive_no_banco(self):
        """
        Salvar os arquivos em um banco de dados
        """
        arquivo = open('../arquivos/tdrive.csv')
        cursor = self.conexao.cursor()
        cont = 0
        for linha in arquivo:
            linha = linha.split(';')
            cursor.execute("INSERT INTO tdrive (taxista_id, datetime, longitude, latitude) values (%s, %s, %s, %s);", [linha[0], linha[1], linha[2], linha[3]])
            cont += 1
            print("A qtd está em {}".format((cont/17662983) * 100))
        arquivo.close()
        self.conexao.commit()
        cursor.close()
    def update_row(self, linha, nova_posicao):
        """
        Atualizar uma linha para a nova_posicao
        """
        linha = linha
        nova_posicao = nova_posicao
        cursor = self.conexao.cursor()
        cursor.execute("UPDATE tdrive SET longitude = {}, latitude = {} WHERE id = {}".format(nova_posicao.longitude, nova_posicao.latitude, linha[0]))
        cursor.commit()
        self.conexao.commit()
        cursor.close()
# conexao = ConnectionFactory().getConection()
# tdrive = tdriveDAO(conexao)
# tdrive.salvar_tdrive_no_banco()
# conexao.close()
