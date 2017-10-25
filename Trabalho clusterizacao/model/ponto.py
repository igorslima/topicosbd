class Ponto:
    def __init__(self, id, longitude, latitude):
        self.id = id
        self.longitude = longitude
        self.latitude = latitude
    def __str__(self):
        return("id: {}, longitude: {}, latitude: {}".format(self.id, self.longitude, self.latitude))