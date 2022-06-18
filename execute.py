from Objetos import Kmeans, DataBase
from Animacoes import run_animation_2d
import sys
import copy


arrayResult = []
dataBase = DataBase()
    

def iterate(kmeans):
    
    for iteration in range(kmeans.iterations):
        kmeans.completed_iterations += 1
        kmeans.classify_samples()
        kmeans.move_centroids()
        if not kmeans.has_moved:
            kmeans.calc_total_distance()
            return kmeans
    kmeans.calc_total_distance()
    return kmeans

#necessary arguments in kmeans
def execute_k_means(clusters=4, minimum_movement=0.0000001, executions=20, iteracoes=1000, animation=False, animation_speed=500):
    if animation:
        kmeans = Kmeans(clusters, iteracoes, minimum_movement, dataBase)
        kmeans.generate_random_positions()
        run_animation_2d(kmeans, animation_speed)
    else:
        total_shortest_distance = sys.maxsize
        best_execution = 0

        #getting shortest distance and best execution
        for exec in range(executions):
            kmeans = Kmeans(clusters, iteracoes, minimum_movement, dataBase)
            kmeans.generate_random_positions()
            result = copy.deepcopy(iterate(kmeans))
            arrayResult.append(result)
            if result.total_distance < total_shortest_distance:
                total_shortest_distance = result.total_distance
                best_execution = exec
                print_best_exec = best_execution+1

        #printing arrayResult
        for result in range(executions):
            print("Resultado %d" % (result+1))
            print("Iterações necessárias: %d" % arrayResult[result].completed_iterations)
            print("Distância total: %f \n" % arrayResult[result].total_distance)

        print("Menor distância: %f" % total_shortest_distance)
        print("Na execução: %d" % print_best_exec)
        arrayResult[best_execution].plotar_mapa()

if __name__ == '__main__':
    execute_k_means()