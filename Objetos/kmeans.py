import math
import sys
from Objetos.centroid import Centroid
import numpy as np
import matplotlib.pyplot as plt
import random


class Kmeans:
    def __init__(self, num_centroids, iterations, minimum_movement, database):
        self.num_centroids = num_centroids
        self.centroids = [Centroid(i) for i in range(num_centroids)]
        self.database = database
        self.iterations = iterations
        self.completed_iterations = 0
        self.has_moved = False
        self.minimum_movement = minimum_movement
        self.total_distance = 0

    def generate_random_positions(self):        
        #Function responsible for generating centroid random positions
        
        choosen_positions = random.sample(range(self.database.quantity_neighborhoods), self.num_centroids)
        for centroid in range(self.num_centroids):
            if centroid == 3:
                self.centroids[centroid].position = [-1.3820529975920155, -48.477489181332565]
                self.centroids[centroid].fix = True
            else:
                self.centroids[centroid].generate_random_positions(self.database, choosen_positions[centroid])

    def classify_samples(self):
        #Function responsible for classifying neighborhoods and centroids sample in coordinates
        
        for centroid in range(self.num_centroids):
            self.centroids[centroid].neighborhoods = []
            self.centroids[centroid].quantity_neighborhoods = 0

        for neighborhood in self.database.neighborhoods:
            shortest_distance = sys.maxsize

            for centroid in self.centroids:
                actual_distance = math.sqrt((self.database.neighborhoods[neighborhood]['coordinates'][0] - centroid.position[0]) ** 2 +
                (self.database.neighborhoods[neighborhood]['coordinates'][1] - centroid.position[1]) ** 2)
                
                if actual_distance <= shortest_distance:
                    shortest_distance = actual_distance
                    self.database.neighborhoods[neighborhood]['centroid'] = centroid.name

            for centroid in range(self.num_centroids):
                if self.database.neighborhoods[neighborhood]['centroid'] == centroid:
                    self.centroids[centroid].neighborhoods.append(neighborhood)
                    self.centroids[centroid].quantity_neighborhoods += 1

    def move_centroids(self):
        #Function responsible for moving centroids 
        
        self.has_moved = False
        for centroid in range(self.num_centroids):

            if not self.centroids[centroid].fix:
                new_position = np.zeros(self.database.dimensions)
                quantity_neighborhoods = self.centroids[centroid].quantity_neighborhoods

                for neighborhood in self.centroids[centroid].neighborhoods:
                    for component in range(self.database.dimensions):
                        new_position[component] += self.database.neighborhoods[neighborhood]['coordinates'][component]
                        
                for component in range(self.database.dimensions):
                    moviment = np.copy(new_position[component]/quantity_neighborhoods) - self.centroids[centroid].position[component]
                    if np.abs(moviment) > self.minimum_movement:
                        self.has_moved = True
                    self.centroids[centroid].position[component] = np.copy(new_position[component]/quantity_neighborhoods)

    def calc_total_distance(self):
        '''
        heuristic function
        '''
        for neighborhood in self.database.neighborhoods:
            self.total_distance += math.sqrt((self.database.neighborhoods[neighborhood]['coordinates'][0] - self.centroids[self.database.neighborhoods[neighborhood]['centroid']].position[0]) ** 2 +
            (self.database.neighborhoods[neighborhood]['coordinates'][1] - self.centroids[self.database.neighborhoods[neighborhood]['centroid']].position[1]) ** 2)

    def plotar_mapa(self):
        x0 = []
        y0 = []
        x1 = []
        y1 = []
        x2 = []
        y2 = []
        x3 = []
        y3 = []
        x_centroid = []
        y_centroid = []

        for centroid in range(self.num_centroids):
            x_centroid.append(self.centroids[centroid].position[1])
            y_centroid.append(self.centroids[centroid].position[0])

        for neighborhood in self.database.neighborhoods:
            if self.database.neighborhoods[neighborhood]['centroid'] == 0:
                x0.append(self.database.neighborhoods[neighborhood]['coordinates'][1])
                y0.append(self.database.neighborhoods[neighborhood]['coordinates'][0])
            elif self.database.neighborhoods[neighborhood]['centroid'] == 1:
                x1.append(self.database.neighborhoods[neighborhood]['coordinates'][1])
                y1.append(self.database.neighborhoods[neighborhood]['coordinates'][0])
            elif self.database.neighborhoods[neighborhood]['centroid'] == 2:
                x2.append(self.database.neighborhoods[neighborhood]['coordinates'][1])
                y2.append(self.database.neighborhoods[neighborhood]['coordinates'][0])
            elif self.database.neighborhoods[neighborhood]['centroid'] == 3:
                x3.append(self.database.neighborhoods[neighborhood]['coordinates'][1])
                y3.append(self.database.neighborhoods[neighborhood]['coordinates'][0])

        plt.plot(x_centroid[0], y_centroid[0], 'go',
                 x_centroid[1], y_centroid[1], 'bo', 
                 x_centroid[2], y_centroid[2], 'yo', 
                 x_centroid[3], y_centroid[3], 'ro', 
                 x0, y0, 'g^', 
                 x1, y1, 'b^', 
                 x2, y2, 'y^', 
                 x3, y3, 'r^')
        
        plt.show()