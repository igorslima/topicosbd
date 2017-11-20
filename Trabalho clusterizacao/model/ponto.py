class Ponto:
    def __init__(self, id, longitude, latitude):
        self.id = id
        self.longitude = longitude
        self.latitude = latitude
        self.visitado = False
        self.cluster = None
        self.iscore = False
    def __str__(self):
        return("id: {}, longitude: {}, latitude: {}, visitado: {}, cluster: {}".format(self.id, self.longitude, self.latitude, self.visitado, self.cluster))