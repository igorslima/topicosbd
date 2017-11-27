from collections import defaultdict
class Graph:
    def __init__(self):
        self.vertices = list()
        self.arestas = defaultdict(list)
        self.pesos = {}
    
    def get_vertices(self):
        return self.vertices
    
    def add_vertice(self, vertice):
        self.vertices.append(vertice)

    def add_aresta(self, from_vertice, to_vertice, custo):
        self.arestas[from_vertice].append(to_vertice)
        self.pesos[(from_vertice, to_vertice)] = custo

    def __str__(self):
        string = "Vertices: " + str(self.vertices) + "\n"
        string += "Atestas: " + str(self.arestas) + "\n"
        string += "Pesos: " + str(self.pesos)
        return string