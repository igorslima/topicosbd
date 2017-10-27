from graph.grafo import Graph
from model.aresta import Aresta
from model import ponto, vertice
from dao.caminhoDAO import CaminhoDAO
from dao.tdrive import TdriveDAO
from dao.conexao import ConnectionFactory
from math import sqrt
import math
import sys

#realiza o MapMatching
def map_matching(pontos, tdrive):
    dicionario = dict()
    for row in tdrive:
        dicionario[row[0]] = find_mais_proximo(row, pontos)
    return dicionario

#encontra o vertice mais próximo
def find_mais_proximo(row, pontos):
    menor_dist = sys.maxsize
    ponto_mais_proximo = None
    for ponto in pontos:
        dist = distancia_euclidiana(row[3], row[4], ponto.longitude, ponto.latitude)
        if dist < menor_dist:
            menor_dist = dist
            ponto_mais_proximo = ponto.id
    return ponto_mais_proximo

#encontra a distancia euclidiana de (x1,y2) para (y1,y2)
def distancia_euclidiana(x1, y1, x2, y2):
    return sqrt(pow(x1-x2, 2) + pow(y1-y2,2))

#pega os caminhos do banco e coloca em um grafo
def base_para_grafo(caminhos):
    grafo = Graph()
    for caminho in caminhos:
        grafo.add_vertice(caminho.id)
        grafo.add_aresta(caminho.inicio, caminho.fim, caminho.custo)      
    return grafo


def dijkstra(graph, inicio):
    dist = []
    for vertice in graph.vertices:
        dist.append(float('inf'))
    dist[inicio-1] = 0
    queue = graph.vertices
    while len(queue) > 0:
        u = min(queue)
        queue.remove(u)
        for v in grafo.arestas[u]:
            print("u: {}".format(u))
            alt = dist[u-1] + grafo.pesos[(u,v)]
            print("v: {}".format(v))
            print("Tamanho dist: {}".format(len(dist)))
            if alt < dist[v-1]:
                print("oi")
                dist[v-1] = alt
    return dist
        
grafo = Graph()
for i in range(6):
    #print(i+1)
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

print(grafo)
print(dijkstra(grafo, 1))