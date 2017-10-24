from graph.grafo import Graph
from model import ponto, aresta, vertice
from dao import tdrive
from math import sqrt

import sys

def map_matching(pontos, tdrive):
    lista = []
    for row in tdrive:
        lista.append(find_mais_proximo(row, pontos))
    return lista

def find_mais_proximo(row, pontos):
    menor_dist = sys.maxsize
    ponto_mais_proximo = None
    for ponto in pontos:
        dist = distancia_euclidiana(row[3], row[4], ponto.longitude, ponto.latitude)
        if dist < menor_dist:
            menor_dist = dist
            ponto_mais_proximo = ponto.id
    return (row[0], ponto_mais_proximo)

def distancia_euclidiana(x1, y1, x2, y2):
    return sqrt(pow(x1-x2, 2) + pow(y1-y2,2))

def base_para_grafo(tdrive_dao):
    grafo = Graph()
    print(grafo)
    for row in tdrive:
        grafo.add_vertice(row)       
#base_para_grafo("oi")

# map_matche = map_matching(pontos, tdrive)
# 