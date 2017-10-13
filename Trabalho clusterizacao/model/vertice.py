class Vertice:
    def __init__(self,id,ponto):
        self.id = id
        self.ponto = ponto
        self.proximoVertice = None

    def setProximoVertice(self, proximoVertice):
        self.proximoVertice = proximoVertice