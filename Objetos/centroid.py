import numpy as np

class Centroid:
    def __init__(self, name, fix=False):
        self.name = name
        self.position = [0, 0]
        self.neighborhoods = []
        self.quantity_neighborhoods = 0
        self.fix = fix

    def __repr__(self):
        return '%d' %self.fix

    def generate_random_positions(self, bd, random_position):
        neighborhoods = list(bd.neighborhoods)
        posicao_centroide = bd.neighborhoods[neighborhoods[random_position]]['coordinates']
        self.position = list(posicao_centroide)