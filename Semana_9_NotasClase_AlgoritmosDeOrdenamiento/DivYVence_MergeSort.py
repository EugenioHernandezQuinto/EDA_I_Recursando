#Implementación de Merge sort

#Fusiona dos subarreglos de arr[].
#El primer subarray es arr [l..m]
#El segundo subarray es arr [m + 1..r]
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    #Se crean arreglos temporales
    #int L[n1], R[n2];

    #Copie datos en arreglos temporales L[] y R[]
    for i in range(0, n1, 1):
        L[i] = arr[l + i]
    for j in range(0, n2, 1):
        R[j] = arr[m + 1 + j]

    #Se combinan los arreglos temporales de nuevo en arr[l..r]
    i = 0 #Índice inicial del primer subarreglo
    j = 0 #Índice inicial del segundo subarreglo
    k = l #Índice inicial del subarreglo combinado
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1

    #Se copian los elementos restantes de L[], si hay alguno
    while i < n1:
        arr[k] = L[i]
        i+=1
        k+=1

    #Se copian los elementos restantes de R[], si hay alguno
    while j < n2:
        arr[k] = R[j]
        j+=1
        k+=1

#l es para el índice izquierdo y r es el índice derecho del subarreglo de arr que se ordenará 
def mergeSort(arr, l, r):
    if l < r:
        #Igual que (l+r)/2, pero evita el desbordamiento para grandes l y h
        m = l + (r - l) // 2 #hay que checar queno haya pez con la división

        #Ordenar la primera y la segunda mitad
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

#Función para imprimir
def printArray(A, size):
    for i in range (0, size, 1):
        print(A[i]) #según yo si se puede, por qu elas listas tienen índices
    print("\n")

# Función main
arr = [12, 11, 13, 5, 6, 7] #es una lista no un arreglo
arr_size = 6

print("El arreglo dado es: \n");
printArray(arr, arr_size);
    
mergeSort(arr, 0, arr_size - 1);

print("\nEl arreglo ordenado es: \n");
printArray(arr, arr_size);
