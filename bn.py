def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1
# datos de prueba
lista_desordenada = [4, 2, 5, 1, 3]
lista_ordenada = sorted(lista_desordenada)
objetivo_presente = 3
objetivo_ausente = 6

# Pruebas de Búsqueda Binaria
print(busqueda_binaria(lista_ordenada, objetivo_presente))    # retornar 2
print(busqueda_binaria(lista_ordenada, objetivo_ausente))     # retornar -1
