print("K Yaswanth Veer 192110117")

import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node, cost):
        self.edges[from_node].append((to_node, cost))
        self.edges[to_node].append((from_node, cost))

def greedy_best_first_search(graph, start, goal):
    open_list = [(heuristic(start, goal), start)]
    came_from = {}
    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor, _ in graph.edges[current]:
            if neighbor not in came_from:
                came_from[neighbor] = current
                heapq.heappush(open_list, (heuristic(neighbor, goal), neighbor))

    return None

def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

if __name__ == "__main__":
    graph = Graph()
    graph.add_node((0, 0))
    graph.add_node((1, 0))
    graph.add_node((1, 1))
    graph.add_node((2, 0))
    graph.add_edge((0, 0), (1, 0), 1)
    graph.add_edge((1, 0), (1, 1), 2)
    graph.add_edge((1, 0), (2, 0), 3)
    graph.add_edge((1, 1), (2, 0), 4)

    start = (0, 0)
    goal = (2, 0)

    path = greedy_best_first_search(graph, start, goal)
    if path:
        print("Shortest path:", path)
    else:
        print("No path found.")
