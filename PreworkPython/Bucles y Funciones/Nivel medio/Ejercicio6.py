'''
Ejercicio: Define una función que tome una lista y un número n, y retorne los primeros n elementos de la lista.
'''
def primeros_n_elementos(lista, n):
    return lista[:n]

mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 5
print("Los primeros", n, "elementos de la lista son:", primeros_n_elementos(mi_lista, n))
