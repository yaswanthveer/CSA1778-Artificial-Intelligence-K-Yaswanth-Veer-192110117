import itertools
import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def total_distance(route, cities):
    dist = 0
    for i in range(len(route) - 1):
        dist += euclidean_distance(cities[route[i]], cities[route[i+1]])
    dist += euclidean_distance(cities[route[-1]], cities[route[0]])
    return dist

def brute_force_tsp(cities):
    num_cities = len(cities)
    min_distance = float('inf')
    optimal_route = None
    
    for route in itertools.permutations(range(num_cities)):
        distance = total_distance(route, cities)
        if distance < min_distance:
            min_distance = distance
            optimal_route = route
    
    return optimal_route, min_distance

if __name__ == "__main__":
    cities = [(0, 0), (1, 3), (2, 1), (4, 4), (6, 2)]
    
    optimal_route, min_distance = brute_force_tsp(cities)
    
    print("Optimal Route:", optimal_route)
    print("Minimum Distance:", min_distance)
