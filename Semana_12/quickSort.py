# Implementación de QuickSort en C

# Función para intercambiar dos elementos
def swap(lista, menor, mayor): 
    temp = lista[menor] 
    lista[menor]= lista[mayor]
    lista[mayor]= temp

# Particionar el arreglo usando el último elemento como pivote
def partition(lista, low, high):
    # Elegir el pivote
    pivot = lista[high]

    # Índice de elemento más pequeño e indica
    # la posición correcta del pivote encontrada hasta ahora
    i = low - 1
    for j in range (low, high):
        # Si el elemento actual es más pequeño que el pivote
        if (lista[j] < pivot):
            # Índice de incremento del elemento más pequeño
            i+=1
            swap(lista, i, j)

    swap(lista, i + 1, high)
    return (i + 1)

# Función que implementa QuickSort
# arr[] --> Arreglo a ordenar,
# low --> ïndice inicial,
# high --> Índice final
def quickSort(lista, low, high):
    if low < high:
        # pi es índice de partición, arr[p]
        # ahora está en el lugar correcto
        pi = partition(lista, low, high)

        # Ordenar por separado los elementos antes de la
        # partición y después de la partición
        quickSort(lista, low, pi - 1)
        quickSort(lista, pi + 1, high)


lista = [10, 7, 8, 9, 1, 5]
N=6

#Function call
quickSort(lista, 0, N - 1)
print("Sorted array: {}".format(lista))
