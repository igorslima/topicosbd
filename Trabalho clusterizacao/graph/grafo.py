from collections import defaultdict
import math
import sys
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

    def __str__(self):
        string = "Vertices: " + str(self.vertices) + "\n"
        string += "Atestas: " + str(self.arestas) + "\n"
        string += "Pesos: " + str(self.pesos)
        return string




def dijkstra(graph, inicio):
    S = set()

    delta = dict.fromkeys(list(graph.vertices), math.inf)
    previous = dict.fromkeys(list(graph.vertices), None)

    delta[inicio] = 0

    while S != graph.vertices:
        v = min((set(delta.keys()) - S), key=delta.get)

        for neighbor in set(graph.arestas[v]) - S:
            new_path = delta[v] + graph.pesos[v,neighbor]

            if new_path < delta[neighbor]:
                delta[neighbor] = new_path
                previous[neighbor] = v
        S.add(v)
		
    return (delta, previous)


def dbscan(grafo, eps, min_points):
    c = 0
    pass
    #c=0
    #escolher um ponto no data set 
    #para cada ponto não visitado no dataset:
    #   t = pegar no mínimo min_points no data_set que estão a no máximo eps (caso eles estejam a menos que eps euclidiana) não é necessário fazer dikstra
    #   marque todos os pontos p em t como fazendo parte do cluster c
    #   para cada ponto em t:
    #       expandir(t, min_points, eps, c)
    #   c = c + 1

def expandir(grafo, t, min_points, eps, c):
    pass    
    #t = pegar todos os pontos que estão dento de eps, caso eles tenham min_points
    #marcar eles fazendo parto do cluster c
    #expandir(grafo, t, min_points, eps, c)
"""

passar os pontos do tdrive para um grafo
depois de salvar todos os ponto 



























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