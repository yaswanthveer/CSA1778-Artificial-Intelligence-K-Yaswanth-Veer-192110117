print("K Yaswanth Veer 192110117")

class MapColoring:
    def __init__(self, graph, colors):
        self.graph = graph
        self.colors = colors
        self.coloring = {}

    def is_valid(self, vertex, color):
        for neighbor in self.graph[vertex]:
            if neighbor in self.coloring and self.coloring[neighbor] == color:
                return False
        return True

    def color_map(self, vertex):
        if vertex is None:
            return True
        
        for color in self.colors:
            if self.is_valid(vertex, color):
                self.coloring[vertex] = color
                if self.color_map(self.get_uncolored_vertex()):
                    return True
                self.coloring.pop(vertex)
        
        return False

    def get_uncolored_vertex(self):
        for vertex in self.graph:
            if vertex not in self.coloring:
                return vertex
        return None

if __name__ == "__main__":
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'C'],
        'C': ['A', 'B', 'D'],
        'D': ['A', 'C']
    }
    
    colors = ['Red', 'Green', 'Blue']

    map_coloring = MapColoring(graph, colors)
    if map_coloring.color_map(map_coloring.get_uncolored_vertex()):
        print("Map coloring solution:")
        for vertex, color in map_coloring.coloring.items():
            print(f"{vertex}: {color}")
    else:
        print("No valid map coloring solution found.")
