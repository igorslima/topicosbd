class Vertice:
    def __init__(self, taxi_id, date_time, longitude, latitude):
        self.taxi_id = taxi_id
        self.date_time = date_time
        self.longitude = longitude
        self.latitude = latitude
    def get_taxi_id(self):
        return self.taxi_id

    def get_date_time(self):
        return self.date_time

    def get_longitude(self):
        return self.longitude

    def get_latitude(self):
        return self.latitude