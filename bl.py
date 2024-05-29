def busqueda_lineal(lista, objetivo):
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice
    return -1
#  datos de prueba
lista_desordenada = [4, 2, 5, 1, 3]
lista_ordenada = sorted(lista_desordenada)
objetivo_presente = 3
objetivo_ausente = 6

# Pruebas de Búsqueda Lineal
print(busqueda_lineal(lista_desordenada, objetivo_presente))  # retornar 4
print(busqueda_lineal(lista_desordenada, objetivo_ausente))   # retornar -1

