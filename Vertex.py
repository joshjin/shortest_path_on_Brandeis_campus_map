import sys


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}
        self.prev = None
        self.next = {}
        self.dist_to_orgn = 99999
        self.dist_to_prev = 99999

    # record prev node
    def set_prev(self, prev):
        self.prev = prev

    def set_next(self, next):
        self.next.append(next)

    # record dist to previous node
    def set_dist_to_orgn(self, dist):
        self.dist_to_orgn = dist

    def set_dist_to_prev(self, dist):
        self.dist_to_prev = dist

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connected_to]) +\
               ' with weight: ' + str([self.get_weight(x) for x in self.connected_to]) +\
               ' with length ' + str(self.get_dist_to_orgn()) +\
               ' with prev ' + str(self.get_prev()) +\
               ' with path length ' + str(self.get_dist_to_prev())

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]

    def get_prev(self):
        return self.prev

    def get_next(self):
        return self.next

    def get_dist_to_orgn(self):
        return self.dist_to_orgn

    def get_dist_to_prev(self):
        return self.dist_to_prev