class Vertice:
    def __init__(self,id_vertice, latitude, longitude, lista_adj=[]):
        self.id = id_vertice
        self.latitude = latitude
        self.longitude = longitude
        self.lista_adj = lista_adj
    def __str__(self):
        return("id: {}, latitude: {}, logitude: {}, lista_adj: {}".format(self.id, self.latitude, self.logitude, self.lista_adj))
