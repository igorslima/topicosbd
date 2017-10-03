# A aresta vai do vertice1 para o vertice2 custando peso
class Aresta:
    def __init__(self, vertice1, vertice2, peso):
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.peso = peso
    def get_arestas(self):
        return (self.vertice1, self.vertice2)