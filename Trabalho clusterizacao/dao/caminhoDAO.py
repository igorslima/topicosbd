from model.aresta import *
class CaminhoDAO:
    def __init__(self, conexao):
        self.conexao = conexao
    def read_csv_to_db(self):
        cursor = self.conexao.cursor()
        pontos = open("../arquivos/table_roads.csv")
        for p in pontos:
            linha = p.split(';')
            cursor.execute("INSERT INTO caminhos (id_caminho, id_source, id_target, custo) values (%s, %s, %s, %s)",[linha[0], linha[1], linha[2], linha[3]])
        pontos.close()
        cursor.close()
    def select_all(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM caminhos;")
        resultado = cursor.fetchall()
        lista = []
        for r in resultado:
            aresta = Aresta(r[0], r[1], r[2], r[3])
            lista.append(aresta)
        cursor.close()
        return lista


"""
connectionFactory = ConnectionFactory()
conexao = connectionFactory.getConection()
dao = CaminhoDAO(conexao)
dao.select_all()
conexao.commit()
conexao.close()
"""