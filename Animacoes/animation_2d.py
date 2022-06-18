
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

plot2d = 0
anim = 0
kmeans = 0

def animation2D(frame):
    global plot2d, anim, kmeans
    kmeans.classify_samples()
    for removing in plot2d:
        removing.remove()
    plt.xlim(-48.52, -48.38)
    plt.ylim(-1.5, -1.3)
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

    for centroid in range(kmeans.num_centroids):
        x_centroid.append(kmeans.centroids[centroid].position[1])
        y_centroid.append(kmeans.centroids[centroid].position[0])

    for neighborhood in kmeans.database.neighborhoods:
        
        #centroid 0
        if kmeans.database.neighborhoods[neighborhood]['centroid'] == 0:
            x0.append(kmeans.database.neighborhoods[neighborhood]['coordinates'][1])
            y0.append(kmeans.database.neighborhoods[neighborhood]['coordinates'][0])

        #centroid 1
        elif kmeans.database.neighborhoods[neighborhood]['centroid'] == 1:
            x1.append(kmeans.database.neighborhoods[neighborhood]['coordinates'][1])
            y1.append(kmeans.database.neighborhoods[neighborhood]['coordinates'][0])
            
        #centroid 2
        elif kmeans.database.neighborhoods[neighborhood]['centroid'] == 2:
            x2.append(kmeans.database.neighborhoods[neighborhood]['coordinates'][1])
            y2.append(kmeans.database.neighborhoods[neighborhood]['coordinates'][0])

        #centroid 3 = default    
        elif kmeans.database.neighborhoods[neighborhood]['centroid'] == 3:
            x3.append(kmeans.database.neighborhoods[neighborhood]['coordinates'][1])
            y3.append(kmeans.database.neighborhoods[neighborhood]['coordinates'][0])
    
    plot2d = plt.plot(x_centroid[0], y_centroid[0], 'go',
                      x_centroid[1], y_centroid[1], 'bo',
                      x_centroid[2], y_centroid[2], 'yo', 
                      x_centroid[3], y_centroid[3], 'ro', 
                      x0, y0, 'g^', 
                      x1, y1, 'b^', 
                      x2, y2, 'y^', 
                      x3, y3, 'r^')
                      
    kmeans.iterations -= 1
    #plt.title('Iterações faltando: %d' % (kmeans.iterations + 1))
    plt.title('Clusterização Aeroportos')
    kmeans.move_centroids()
    if kmeans.iterations == -1 or not kmeans.has_moved:
        kmeans.calc_total_distance()
        print(f'Distância total: {kmeans.total_distance}')
        anim.event_source.stop()


def run_animation_2d(kmeans2, animation_speed):
    global anim, kmeans, plot2d
    kmeans = kmeans2
    plot2d = plt.plot(0, 0)
    print("Inicializando animação 2D")
    anim = FuncAnimation(plt.gcf(), animation2D, interval=animation_speed, repeat=False)
    plt.show()

