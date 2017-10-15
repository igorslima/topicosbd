class HashMapDAO:
    def __init__(self, conexao):
        self.conexao = conexao
    def inserir_no_banco(self, ponto_id, vertice_id):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO hash_map(ponto_id, vertice_id) VALUES (%s, %s)", [ponto_id, vertice_id])
        cursor.close()