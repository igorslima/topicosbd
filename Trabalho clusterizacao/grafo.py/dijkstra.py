import sys
class Dijkstra:
    def __init__(self, conjunto_vertices, conjunto_aresta):
        self.vertices = conjunto_vertices
        self.arestas = conjunto_aresta
        self.distancias = []

    def dijkstra(self, inicio, fim):
        self.distancias = []
        for vertice in self.vertices:
            self.distancias.append([vertice.id, sys.float_info.max])
    
    def find_vertice(self, id_vertice):
        for vertice in self.vertices:
            if vertice.id == id_vertice:
                return vertice
        return None
    def find_vertices(self, id_vertice):
        lista = []
        for aresta in self.arestas:
            if(aresta.inicio == id_vertice):
                lista.append(aresta)
        return lista