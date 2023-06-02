import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #al parecer no es necesario importar
import random 

times = 0 

def merge(lista, l, m, r): #nota como merge no esta en recursión
#no devueklve nada, ni la lista, pero está bien por que siempre hemos pasado la original
    global times #solo digo que se va a modificar
    n1 = m - l + 1
    n2 = r - m

    Left=[]
    Right=[]

    for i in range(0, n1):
        times+=1
        Left.append(lista[l+i]) 
    for j in range(0, n2):
        times+=1
        Right.insert(j, lista[m + 1 + j]) 
        
    i = 0 
    j = 0 
    k = l 
    while i < n1 and j < n2:
        times+=1
        if Left[i] <= Right[j]:
            lista[k] = Left[i]
            i+=1
        else:
            lista[k] = Right[j]
            j+=1
        k+=1

    while i < n1: #lo que está en un ciclo es constante
        times+=1
        lista[k] = Left[i]
        i+=1
        k+=1

    while j < n2:
        times+=1
        lista[k] = Right[j]
        j+=1
        k+=1

def grafiquitaDeMergeSort(lista, l, r): #nota como esta función está en recursión
    if l < r:
        m = l + (r - l) // 2 
        grafiquitaDeMergeSort(lista, l, m)
        grafiquitaDeMergeSort(lista, m + 1, r)
        merge(lista, l, m, r)
    return lista #en teoría siempre hemos pasado la original

TAM = 101
eje_x = list(range(1, TAM, 1)) 

eje_y = []
lista_variable = [] 

for num in eje_x: 
    lista_variable = random.sample(range(0,1000), num) 
    print("Lista desordenada {}".format(lista_variable))
    times = 0
    lista_variable = grafiquitaDeMergeSort(lista_variable, 0, num-1) #envias diferentes listas? nuevas y cada vez más grandes?
    print("Lista ordenada {}".format(lista_variable))
    eje_y.append(times) #time es importante, averigua cuando contar y cuando no
    print("Soy times {}".format(times)) 
    
print("No sé que pez con esta lista {}".format(lista_variable)) #supongo que es la última lista


fig, ax = plt.subplots(facecolor='c', edgecolor='b') 
ax.plot(eje_x, eje_y, marker="o", color="b", linestyle='None') 

ax.set_xlabel("x me dicen")
ax.set_ylabel("y sere")
ax.grid(True)  
ax.legend(["Soy Merge Sort"])

plt.title("Me llaman Merge sort")
plt.show() 

