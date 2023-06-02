#version viiejita
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #al parecer no es necesario importar
import random 

times = 0 

def grafiquitaDeQuickSort(lista): #podiamos ahorrarnos esta función al chile
    quicksort_aux(lista, 0, len(lista)-1)
    return lista 

def quicksort_aux(lista, inicio, fin): #esta en recursión
    if inicio < fin:
        pivote = particion(lista, inicio, fin)
        quicksort_aux(lista, inicio, pivote-1)
        quicksort_aux(lista, pivote+1, fin)

def particion(lista, inicio, fin):
    global times
    
    pivote = lista[inicio]
    #print("Valor del pivote {}".format(pivote))
    izquierda = inicio + 1
    derecha = fin
    #print("índice izquierdo {}".format(izquierda))
    #print("índice derecho {}".format(derecha))

    bandera = False

    while not bandera: 
        times+=1
        while izquierda <= derecha and lista[izquierda] <= pivote:
            times+=1
            izquierda+=1
        while lista[derecha] >= pivote and derecha >= izquierda:
            times+=1
            derecha-=1
        if derecha < izquierda:
            bandera= True
        else:
            temp = lista[izquierda]
            lista[izquierda] = lista[derecha]
            lista[derecha] = temp
    #print(lista) #pa' qué

    temp = lista[inicio]
    lista[inicio] = lista[derecha]
    lista[derecha] = temp
    return derecha

TAM = 101
eje_x = list(range(1, TAM, 1)) 
eje_y = []
lista_variable = [] #importante ver que es una lista, y que es global

for num in eje_x: 
    lista_variable = random.sample(range(0,1000), num) #te da valores ordenados
    print("Lista desordenada {}".format(lista_variable))#aquí se imprimiría la lista desordenada
    times = 0 #mide cuanto le toma ordenar cada vez una lista más grande #reinicia los times #supongo que por que este for no esta en una función, no tengo que poner global times
    lista_variable = grafiquitaDeQuickSort(lista_variable) #en teoría envie la original, pero weno, tengo que recibir algo
    print("Lista ordenada {}".format(lista_variable))
    eje_y.append(times) #pienso yo que hace menos times
    print("Soy times {}".format(times)) #no sé por que cambia times en diferentes ejecuciones
    
print("No sé que pez con esta lista {}".format(lista_variable)) #supongo que es la última lista


fig, ax = plt.subplots(facecolor='c', edgecolor='b') 
ax.plot(eje_x, eje_y, marker="*", color="m", linestyle='None') 

ax.set_xlabel("x me dicen")
ax.set_ylabel("y sere")
ax.grid(True)  
ax.legend(["Soy Quick Sort"])

plt.title("Me llaman Quick sort")
plt.show() 

#el qu emi gráfica salga bien depende de times.

#+, -, *, //, =, if, call se consideran one step