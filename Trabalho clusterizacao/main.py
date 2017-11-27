from graph.grafo import Graph
from model.aresta import Aresta
from model.vertice import Vertice
from model import ponto, vertice
from dao.caminhoDAO import CaminhoDAO
from dao.tdrive import TdriveDAO
from dao.pontoDAO import PontoDAO
from dao.conexao import ConnectionFactory
from math import sqrt
import math
import sys
import csv

"""
realiza o MapMatching
"""
def map_matching(pontos, tdrive):
    dicionario = dict()
    cont = 1
    for row in tdrive:
        print("qtd: {}".format(cont/len(tdrive) *100))
        dicionario[row[0]] = find_mais_proximo(row, pontos)
        cont += 1
    return dicionario

def find_mais_proximo(row, pontos):
    menor_dist = sys.maxsize
    ponto_mais_proximo = None
    for ponto in pontos:
        dist = distancia_euclidiana(row[3], row[4], ponto.longitude, ponto.latitude)
        if dist < menor_dist:
            menor_dist = dist
            ponto_mais_proximo = ponto.id
    return ponto_mais_proximo

def distancia_euclidiana(x1, y1, x2, y2):
    return sqrt(pow(x1-x2, 2) + pow(y1-y2,2))

def base_para_grafo(topologia, pontos):
    grafo = Graph()
    cont = 0
    for aresta in topologia:
        print(cont/len(topologia))
        cont += 1
        if aresta.inicio not in grafo.vertices:
#            inicio = Vertice(aresta.inicio, pontos[i][0], pontos[i][1])
            grafo.add_vertice(aresta.inicio)
        if aresta.fim not in grafo.vertices:
            grafo.add_vertice(aresta.fim)
        grafo.add_aresta(aresta.inicio, aresta.fim, aresta.custo)
    return grafo

def dijkstra(grafo, source):
    dist = []
    for vertice in grafo.vertices:
        dist.append(float('inf'))
    dist[source-1] = 0
    queue = grafo.vertices.copy()
    lista = list(queue)
    while len(queue) > 0:
        u = min(queue)
        queue.remove(u)
        for v in grafo.arestas[u]:
            alt = dist[u-1] + grafo.pesos[(u,v)]
            if alt < dist[v-1]:
                dist[v-1] = alt
    dicionario = dict()
    for x in range(len(lista)):
        dicionario[lista[x]] = dist[x]
    return dicionario

def DBSCAN(grafo, eps, min_points):
    cluster_id = 0
    for vertice in grafo.vertices:
        if vertice.visitado == False:
            vertice.visitado = True
            vertice.iscore = False
            pontos_vizinhos = regionQuery(vertice, grafo, eps)
            if(len(pontos_vizinhos) < min_points):
                vertice.cluster = "NOISE"
            else:
                vertice.iscore = True
                cluster_id += 1
                expand_cluster(vertice, pontos_vizinhos, cluster_id, eps, min_points)

def expand_cluster(ponto, pontos_vizinhos, cluster_id, eps, min_points):
    ponto.cluster_id = cluster_id
    for p in pontos_vizinhos:
        if p.visitado == False:
            p.visitado = True
            pontos_vizinhos_de_p = regionQuery(p, grafo, eps)
            if len(pontos_vizinhos_de_p) >= min_points:
                for _ponto in pontos_vizinhos_de_p:
                    if _ponto not in pontos_vizinhos:
                        pontos_vizinhos.append(_ponto)
            if p.cluster_id == None:
                p.cluster_id = cluster_id

def regionQuery(ponto, grafo, eps):
    lista = []
    resultado_dijkstra = dijkstra(grafo, ponto)
    for resultado in resultado_dijkstra:
        if resultado > eps:
            lista.append(resultado)
    return lista

def exportar_csv(grafo):
    arquivo = open("output.csv", 'w', newline='')
    campos = ['student_id', 'weekday', 'hour', 'latitude', 'longitude', 'cluster', 'iscore']
    writer = csv.DictWriter(arquivo, fieldnames=campos)
    writer.writeheader()
    for ponto in grafo.vertices:
        writer.writerow({'student_id' : '375082', 'weekday' : '02', 'hour' : '23', 'latitude' : ponto.latitude, 'longitude' : ponto.longitude, 'cluster' : ponto.cluster, 'iscore' : ponto.iscore})


grafo = Graph()
for x in range(7):
    grafo.add_vertice(x+1)
grafo.add_aresta(1,2,2)
grafo.add_aresta(2,4,3)
grafo.add_aresta(2,5,1)
grafo.add_aresta(1,3,4)
grafo.add_aresta(3,7,2)
# grafo.add_aresta(5,4,1)
# print(dijkstra(grafo, 1))
conexao = ConnectionFactory().getConection()
caminhosDao = CaminhoDAO(conexao)
grafo = base_para_grafo(caminhosDao.select_all(), "postos")
print(grafo)