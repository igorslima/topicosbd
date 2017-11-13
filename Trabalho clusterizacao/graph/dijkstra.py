class dijkstra:
    def __init__(self, grafo):
        self.grafo = grafo
    
    def run(self, initial):
        visitados = {initial: 0}
        vertices = set(self.grafo.vertices)
        while vertices:
            min_vertice = None
            for node in vertices:
                if node in visitados:
                    if min_vertice is None:
                        min_vertice = node
                    elif visitados[node] < visitados[min_vertice]:
                        min_vertice = node
            if min_vertice is None:
                break
            vertices.remove(min_vertice)
            peso_atual = visitados[min_vertice]

            for edge in self.grafo.arestas[min_vertice]:
                peso = peso_atual + self.grafo.pesos[(min_vertice, edge)]
                if edge not in visitados or peso < visitados[edge]:
                    visitados[edge] = peso       
        return visitados