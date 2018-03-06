class distAndTime:
    def __init__(self):
        self.i = 0
        self.time = 0
        self.dist = 0

    def inc_i(self):
        self.i = self.i + 1

    def add_time(self, time):
        self.time = self.time + time

    def add_dist(self, distance):
        self.dist = self.dist + distance

    def get_time(self):
        return self.time

    def get_dist(self):
        return self.dist

    def get_i(self):
        return self.i