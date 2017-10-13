from conexao import ConnectionFactory

class CaminhoDAO:
    def __init__(self, cursor):
        self.cursor = cursor
    
    def read_csv_to_db(self):
        pontos = open("../arquivos/table_roads.csv")
        for p in pontos:
            linha = p.split(';')
            self.cursor.execute("INSERT INTO caminhos (id_caminho, id_source, id_target, custo) values (%s, %s, %s, %s)",[linha[0], linha[1], linha[2], linha[3]])
        pontos.close()

connectionFactory = ConnectionFactory()
conexao = connectionFactory.getConection()
cursor = conexao.cursor()
dao = CaminhoDAO(cursor)
dao.read_csv_to_db()
conexao.commit()
cursor.close()
conexao.close()