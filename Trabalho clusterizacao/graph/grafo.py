from collections import defaultdict
import math
import sys
from dijkstra import *
# sys.path.append('..')
# from dao.caminhoDAO import *
# from dao.conexao import ConnectionFactory

class Graph:
    def __init__(self):
        self.vertices = set()
        self.arestas = defaultdict(list)
        self.pesos = {}
      
    def add_vertice(self, vertice):
        self.vertices.add(vertice)

    def add_aresta(self, do_vertice, para_vertice, custo):
        if do_vertice == para_vertice: 
            pass
        self.arestas[do_vertice].append(para_vertice)
        self.pesos[(do_vertice, para_vertice)] = custo


    # def dijkstra(self, start, end):
    #     final_distances = {}
    #     predecessor = {}
    #     Q = priorityDictionary()
    #     q[start] = 0
    #     for v in Q:
    #         final_distances[v] = q[v]
    #         if v == end:
    #             break



    def make_dijkstra(self, source, target):
        assert source in self.vertices
        dist = {vertice: sys.maxsize for vertice in self.vertices}
        prev = {vertice: None for vertice in self.vertices}
        dist[source] = 0
        q = self.vertices.copy()
        vizinhos = {vertice: set() for vertice in self.vertices}
        for vertice in self.vertices:
            pass

    def __str__(self):
        string = "Vertices: " + str(self.vertices) + "\n"
        string += "Atestas: " + str(self.arestas) + "\n"
        string += "Pesos: " + str(self.pesos)
        return string
    

grafo = Graph()
for i in range(6):
    #print(i+1)
    print(i+1)
    grafo.add_vertice(i+1)
grafo.add_vertice(7)
grafo.add_aresta(1,2,1)
grafo.add_aresta(1,6,2)
grafo.add_aresta(2,3,2)
grafo.add_aresta(2,4,1)
grafo.add_aresta(3,5,2)
grafo.add_aresta(4,5,1)
grafo.add_aresta(6,4,1)
grafo.add_aresta(6,5,1)
dijkstra = dijkstra(grafo)
print(dijkstra.run(1))

# def dijkstra(graph, inicio):
#     S = set()

#     delta = dict.fromkeys(list(graph.vertices), math.inf)
#     previous = dict.fromkeys(list(graph.vertices), None)

#     delta[inicio] = 0

#     while S != graph.vertices:
#         v = min((set(delta.keys()) - S), key=delta.get)

#         for neighbor in set(graph.arestas[v]) - S:
#             new_path = delta[v] + graph.pesos[v,neighbor]

#             if new_path < delta[neighbor]:
#                 delta[neighbor] = new_path
#                 previous[neighbor] = v
#         S.add(v)
		
#     return (delta, previous)






















"""
connectionFactory = ConnectionFactory()
conexao = connectionFactory.getConection()
dao = CaminhoDAO(conexao)
dados = dao.select_all()
grafo = Graph()
for aresta in dados:
    grafo.add_vertice(aresta.inicio)
for aresta in dados:
    print(aresta.custo)
    grafo.add_aresta(aresta.inicio, aresta.fim, aresta.custo)
conexao.commit()
conexao.close()
"""