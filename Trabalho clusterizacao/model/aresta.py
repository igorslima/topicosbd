class Aresta:
    def __init__(self, id, inicio, fim, custo):
        self.id = id
        self.inicio = inicio
        self.fim = fim
        self.custo = custo
    def __str__(self):
        return("id: {}, inicio: {}, fim: {}, custo: {}".format(self.id, self.inicio, self.fim, self.custo))
