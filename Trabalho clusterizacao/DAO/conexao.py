import psycopg2

class ConnectionFactory:
    def __init__(self):
        pass
    
    def getConection(self):
        try:
            conexao = psycopg2.connect("dbname='topicos_bd' user='postgres' host='localhost' password='postgres'")
            return conexao
        except:
            print("Erro ao conectar com o banco")
            return None
    def closeConnection(self):
        pass
'''            
connectionFactory = ConnectionFactory()
con = connectionFactory.getConection()
cursor = con.cursor()
cursor.execute("INSERT INTO vertices(id_taxista, longitude, latitude) VALUES (0, 0, 0);")

con.commit()
cursor.close()
con.close()
'''