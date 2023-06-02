#versión nueva
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import random 

times = 0 

def swap(lista, menor, mayor): 
    temp = lista[menor] 
    lista[menor]= lista[mayor]
    lista[mayor]= temp

def partition(lista, low, high):
    global times
    pivot = lista[high]
    i = low - 1
    for j in range (low, high):
        times+=1
        if (lista[j] < pivot):
            i+=1
            swap(lista, i, j)
    swap(lista, i + 1, high)
    return i + 1

def grafiquitaDeQuickSort(lista, low, high):
    if low < high:
        pi = partition(lista, low, high)

        grafiquitaDeQuickSort(lista, low, pi - 1)
        grafiquitaDeQuickSort(lista, pi + 1, high)
    return lista


TAM = 101
eje_x = list(range(1, TAM, 1)) 
eje_y = []
lista_variable = [] 

for num in eje_x: 
    lista_variable = random.sample(range(0,1000), num) 
    print("Lista desordenada {}".format(lista_variable))
    times = 0 
    lista_variable = grafiquitaDeQuickSort(lista_variable, 0, num-1) 
    print("Lista ordenada {}".format(lista_variable))
    eje_y.append(times) #times va a cambiar por que los elementos desordenados no son los mismos, puede que a veces sea más "fácil" de sortear que en otras ocasiones
    print("Soy times {}".format(times)) 
    
print("No sé que pez con esta lista {}".format(lista_variable)) 


fig, ax = plt.subplots(facecolor='c', edgecolor='b') 
ax.plot(eje_x, eje_y, marker="*", color="m", linestyle='None') 

ax.set_xlabel("x me dicen")
ax.set_ylabel("y sere")
ax.grid(True)  
ax.legend(["Soy Quick Sort"])

plt.title("Me llaman Quick sort")
plt.show() 
