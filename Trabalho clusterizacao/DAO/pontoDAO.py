from conexao import ConnectionFactory

class PontoDAO:
    def __init__(self, cursor):
        self.cursor = cursor
        
    def read_csv_to_db(self):
        pontos = open("../arquivos/table_vertices.csv")
        for p in pontos:
            linha = p.split(';')
            self.cursor.execute("INSERT INTO public.pontos (id_ponto, longitude, latitude) values (%s, %s, %s)",[linha[0], linha[1], linha[2]])
        pontos.close()

connectionFactory = ConnectionFactory()
conexao = connectionFactory.getConection()
cursor = conexao.cursor()
dao = PontoDAO(cursor)
dao.read_csv_to_db()
conexao.commit()
cursor.close()
conexao.close()