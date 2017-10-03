from vertice import Vertice

def file_to_vert_list(file):
    lista = []
    for line in open(file):
        linha = line.split(',')
        vertice = Vertice(linha[0], linha[1], linha[2], linha[3])
        lista.append(vertice)
    return lista

lista = file_to_vert_list('1.txt')
l = lista[0]
print(l.get_longitude()) 