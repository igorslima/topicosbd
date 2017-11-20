from graph.grafo import Graph
from model.aresta import Aresta
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

"""
encontra o vertice mais próximo
"""
def find_mais_proximo(row, pontos):
    menor_dist = sys.maxsize
    ponto_mais_proximo = None
    for ponto in pontos:
        dist = distancia_euclidiana(row[3], row[4], ponto.longitude, ponto.latitude)
        if dist < menor_dist:
            menor_dist = dist
            ponto_mais_proximo = ponto.id
    return ponto_mais_proximo

"""
encontra a distancia euclidiana de (x1,y2) para (y1,y2)
"""
def distancia_euclidiana(x1, y1, x2, y2):
    return sqrt(pow(x1-x2, 2) + pow(y1-y2,2))

"""
passa a base para um grafo
"""
def base_para_grafo(caminhos):
    grafo = Graph()
    for aresta in caminhos:
        if(aresta.inicio not in grafo.vertices):
            grafo.add_vertice(aresta.inicio)
        if(aresta.fim not in grafo.vertices):
            grafo.add_vertice(aresta.fim)
        grafo.add_aresta(aresta.inicio, aresta.fim, aresta.custo)      
    return grafo

'''
Retorna um dicionário com a menor distância do source para todos os demais vertices do grafo 
'''
def dijkstra(graph, source):
    dist = []
    print(graph)
    for vertice in graph.vertices:
        dist.append(float('inf'))
    dist[source-1] = 0
    queue = graph.vertices.copy()
    lista = list(queue)
    while len(queue) > 0:
        u = min(queue)
        queue.remove(u)
        for v in graph.arestas[u]:
            alt = dist[u-1] + graph.pesos[(u,v)]
            if alt < dist[v-1]:
                dist[v-1] = alt
    dicionario = dict()
    for x in range(len(lista)):
        dicionario[lista[x]] = dist[x]
    return dicionario

def DBSCAN(grafo, eps, min_points, pontos):
    cluster_id = 0
    for vertice in grafo.vertices:
        if pontos[vertice].visitado == False:
            pontos[vertice].visitado = True
            pontos[vertice].iscore = False
            pontos_vizinhos = regionQuery(vertice, grafo, eps)
            if(len(pontos_vizinhos) < min_points):
                pontos[vertice].cluster = "NOISE"
            else:
                pontos[vertice].iscore = True
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
    writer.writeheader() # escrevendo cabeçalho
    for ponto in grafo.vertices:
        writer.writerow({'student_id' : '375082', 'weekday' : '02', 'hour' : '23', 'latitude' : ponto.latitude, 'longitude' : ponto.longitude, 'cluster' : ponto.cluster, 'iscore' : ponto.iscore})

conexao = ConnectionFactory().getConection()
caminhos = CaminhoDAO(conexao).select_all()
pontos = PontoDAO(conexao).select_all()
tdrive = TdriveDAO(conexao).select_all()
dicionario_map_matching = map_matching(pontos, tdrive)
grafo = base_para_grafo(caminhos)
DBSCAN(grafo, 0.004, 10, "dicionario_map_matching")