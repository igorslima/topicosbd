class Vertice:
    def __init__(self,id_row_tdrive, id_ponto):
        self.id = id_row_tdrive
        self.ponto = id_ponto
        self.proximoVertice = None

    def setProximoVertice(self, proximoVertice):
        self.proximoVertice = proximoVertice