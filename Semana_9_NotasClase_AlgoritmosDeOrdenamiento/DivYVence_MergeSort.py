#Implementación de Merge sort

#Fusiona dos subarreglos de arr[].
#El primer subarray es arr [l..m]
#El segundo subarray es arr [m + 1..r]
def merge(lista, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    #Se crean arreglos temporales
    #int L[n1], R[n2];
    Left=[]
    Right=[]

    #Copie datos en arreglos temporales L[] y R[]
    for i in range(0, n1):
        Left.append(lista[l+i]) #dos formas
    for j in range(0, n2):
        Right.insert(j, lista[m + 1 + j]) #dos formas
        

    #Se combinan los arreglos temporales de nuevo en arr[l..r]
    i = 0 #Índice inicial del primer subarreglo
    j = 0 #Índice inicial del segundo subarreglo
    k = l #Índice inicial del subarreglo combinado
    while i < n1 and j < n2:
        if Left[i] <= Right[j]:
            lista[k] = Left[i]
            i+=1
        else:
            lista[k] = Right[j]
            j+=1
        k+=1

    #Se copian los elementos restantes de L[], si hay alguno
    while i < n1:
        lista[k] = Left[i]
        i+=1
        k+=1

    #Se copian los elementos restantes de R[], si hay alguno
    while j < n2:
        lista[k] = Right[j]
        j+=1
        k+=1

#l es para el índice izquierdo y r es el índice derecho del subarreglo de arr que se ordenará 
def mergeSort(lista, l, r):
    if l < r:
        #Igual que (l+r)/2, pero evita el desbordamiento para grandes l y h
        m = l + (r - l) // 2 #hay que checar queno haya pez con la división

        #Ordenar la primera y la segunda mitad
        mergeSort(lista, l, m)
        mergeSort(lista, m + 1, r)
        merge(lista, l, m, r)


# Función main
lista = [12, 11, 13, 5, 6, 7] #es una lista no un arreglo
lista_size = 6

print("El arreglo dado es: \n")
print(lista)
    
mergeSort(lista, 0, lista_size - 1)

print("\nEl arreglo ordenado de mayor a menor es: \n")
print(lista)
