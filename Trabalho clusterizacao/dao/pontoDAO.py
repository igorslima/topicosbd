from model.ponto import *
class PontoDAO:

    def __init__(self, conexao):
        self.conexao = conexao
    # def read_csv_to_db(self):
    #     """
    #     Metodo para colocar todos os pontos no banco
    #     """
    #     cursor = self.conexao.cursor()
    #     pontos = open("../arquivos/table_vertices.csv")
    #     for ponto in pontos:
    #         linha = ponto.split(';')
    #         cursor.execute("INSERT INTO public.pontos (id_ponto, longitude, latitude) values (%s, %s, %s)", [linha[0], linha[1], linha[2]])
    #     pontos.close()
    #     self.conexao.commit()
    #     cursor.close()
    def select_all(self):
        """
        Metodo para selecionar todos os pontos
        """
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM pontos;")
        resultado = cursor.fetchall()
        dicionario = dict()
        for result in resultado:
            dicionario[resultado[0]] = (resultado[1], resultado[2])
        cursor.close()
        return dicionario
