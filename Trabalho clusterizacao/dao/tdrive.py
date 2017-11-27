class TdriveDAO():
    def __init__(self, conexao):
        self.conexao = conexao
    def select_all(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM tdrive WHERE SUBSTRING(datetime, 9,2) = '02' AND SUBSTRING(datetime, 12,2) = '23' AND SUBSTRING(datetime, 15,2) > '55'") # 8752 resultados 
        resultado = cursor.fetchall()
        cursor.close()
        return resultado
    def salvar_tdrive_no_banco(self):
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
        linha = linha
        nova_posicao = nova_posicao
        cursor = self.conexao.cursor()
        cursor.execute("UPDATE tdrive SET longitude = {}, latitude = {} WHERE id = {}".format(nova_posicao.longitude, nova_posicao.latitude, linha[0]))
        cursor.commit()
        self.conexao.commit()
        cursor.close()