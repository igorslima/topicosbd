class Vertice:
    def __init__(self, taxi_id, date_time, longitude, latitude):
        self.taxi_id = taxi_id
        self.date_time = date_time
        self.longitude = longitude
        self.latitude = latitude
    def get_taxi_id(self):
        return int(self.taxi_id)

    def get_date_time(self):
        return str(self.date_time)

    def get_longitude(self):
        return float(self.longitude)

    def get_latitude(self):
        return float(self.latitude)

#vertice = Vertice(1,2,3,4)
#print(type(vertice.get_latitude()))