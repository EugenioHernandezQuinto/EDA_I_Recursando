#Implementación de Selection sort

def swap(lista, menor, mayor): #lista si es arr por que todo se envía por referencia, no importa que le hayas cambiado el nombre
    #me acuerdo que en C si hay swap
    print("x({})".format(menor))
    print("con y({})".format(mayor))
    temp = lista[menor] #temp no guarda índices bro
    lista[menor]= lista[mayor] #reccuerda que las listas no las modificas como un arreglo, o creo que si, ah caray, intentemoslo
    lista[mayor]= temp

def selectionSort(list, n): #minimun es el índice del mínimo
    print("Me enviaste este arreglo: {}".format(list))

    for i in range (0, n-1): #no toca n-1
        minimum = i #min_inx es integer
        print("no sé pa' que te sirva, pero minimum vale {}".format(minimum))
        for j in range (i+1, n): #no toca n
            print("no sé pa' que te sirva, pero j vale {}".format(j))
            if list[j] < list[minimum]: #las listas tienen índices
                print("Entró al famoso if con {}<{}".format(list[j], list[minimum]))
                minimum = j
                print("minimun lo cambio a {}".format(j))

        if minimum != i:
            print("Hizo swap, a continuación te lo muestro: ")
            swap(list, minimum, i) #minimum e i son enteros, guardan indices
            print("Así quedó la lista: {}".format(list))

    print("Arreglo ordenado: {}".format(list))

# Función para imprimir 
"""
def imprimirLista(arr, size):
    for i in range (0, size): #no toca size, y weno sabemos que aumenta de uno en uno
        print(arr[i])#las listas tienen índices
"""

# Función main
if __name__ == "__main__":
    lista = [64, 75, 2, 13, 91] #list son como los arreglos de Python
    n = 5
    selectionSort(lista, n)
