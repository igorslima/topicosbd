class Vertice:
    def __init__(self,id_vertice,ponto):
        self.id = id_vertice
        self.ponto = ponto
        self.proximoVertice = None

    def setProximoVertice(self, proximoVertice):
        self.proximoVertice = proximoVertice