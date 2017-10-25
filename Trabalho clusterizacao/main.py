from graph.grafo import Graph
from model.aresta import Aresta
from model import ponto, vertice
from dao.caminhoDAO import CaminhoDAO
from dao.tdrive import TdriveDAO
from dao.conexao import ConnectionFactory
from math import sqrt

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

