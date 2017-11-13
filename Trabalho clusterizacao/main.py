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


def dijkstra(graph, source, target):
    dist = []
    for vertice in graph.vertices:
        dist.append(float('inf'))
    dist[source-1] = 0
    queue = graph.vertices
    while len(queue) > 0:
        u = min(queue)
        queue.remove(u)
        for v in graph.arestas[u]:
            alt = dist[u-1] + graph.pesos[(u,v)]
            if alt < dist[v-1]:
                dist[v-1] = alt
    return dist

def DBSCAN(grafo, eps, min_points):
    cluster_id = 0
    for ponto in grafo.vertice:
        if ponto.visitado == False:
            ponto.visitado = True
            pontos_vizinhos = regionQuery(ponto, eps)
            if(len(pontos_vizinhos) < min_points):
                ponto.cluster = "NOISE"
            else:
                cluster_id += 1
                expand_cluster(ponto, pontos_vizinhos, cluster_id, eps, min_points)

def expand_cluster(ponto, pontos_vizinhos, cluster_id, eps, min_points):
    ponto.cluster_id = cluster_id
    for p in pontos_vizinhos:
        if p.visitado == False:
            p.visitado = True
            pontos_vizinhos_de_p = regionQuery(p, eps)
            if len(pontos_vizinhos_de_p) >= min_points: # pode repetir vizinhos
                for _ponto in pontos_vizinhos_de_p:
                    pontos_vizinhos.append(_ponto)
            if p.cluster_id == None:
                p.cluster_id = cluster_id
def regionQuery(ponto, tdrive, grafo, eps):
    lista = []
    resultado_dijkstra = dijkstra(grafo, ponto)
    for resultado in resultado_dijkstra:
        if resultado > eps:
            lista.append(res)

    return lista


































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

print(dijkstra(grafo, 1, 3))