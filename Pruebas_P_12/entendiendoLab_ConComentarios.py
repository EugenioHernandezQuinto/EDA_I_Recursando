#%pylab inline

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random #aquí importamos todo random, por que se podía from random import sample y ya usabamos sample en lugar de random.sample

times = 0 #sho pienso que se llama times y no time, pero como vimos, parece que no es necesria declararla

def grafiquitaDeInsertionSort(n_lista): #cada bendito ciclo, le voy a enviar una lista cada vez más grande a esta función
#lista_variable y n_lista representan escencialmente lo mismo
    
    #print("num vale {}".format(num))
    global times #supongo que significa que dentro de la función la voy a cambiar
    #te das cuenta que times es bien inútil, pa' que decir que es global y decir que lo voy a modificar si en digamos el código prinicipal quiero que siga valiendo lo mismo, 0. No lo que pasa es que si te das cuenta, en el digamos main antes de volver a empezar un nuevo ciclo y cambiar times a 0, es asignado a eje_x con un valor que ya tiene desde esta función
    
    for index in range(1, len(n_lista)): #este segundo parámetro de range va a ser desde 1 hasta 100 tocandolo. Entonces este for se va a ajecutar en todo el programa en TOTAL 100 veces, pero esas veces que se va a ajecutar digamos con una duración cada vez más grande
        #print("soy índice {}".format(index))
        times+=1
        actual = n_lista[index] #recuerda que las listas tienen índices
        position = index
        while(position > 0 and n_lista[position-1] > actual): #mi pregunta es cuándo va a ser position menor a cero.
            #print("entré")
            times+=1
            n_lista[position] = n_lista[position-1]
            position-=1
            
        n_lista[position] = actual
    #print("Esta es la rarita lista {}".format(n_lista))    
    return n_lista

TAM = 101
eje_x = list(range(1, TAM, 1)) #range(start, stop, step) supongo que step no era necesario, pero lo dejamos pos por que si
#list() es una función, necesita un ietrable como parámetro. En este caso eje_x vale empezando desde el 1 hasta una antes de TAM, la cual vale 101. Al chile no era necesario crear TAM

#supongo que eje_x es una lista también, y me lo confirma el explorador de variables
eje_y = []
lista_variable = [] #es una lista según yo

for num in eje_x: #supongo que esto es como lo primero a lo que entra después de todas esas declaraciones/inicializaciones
#se ejecuta 100 veces creo, por que va desde el 1 hasta el 100 tocandolo    
    lista_variable = random.sample(range(0,1000), num) #random.sample(secuencia, how_many)  El parámetro secuencia puede ser una lista, tupla, string, en este caso no es ninguno de los anteriores. hown_many es como cuantos elementos quieres que te de, en caso de que quieras varios, van a ser aleatorios. Si te das cuenta num se va haciendo más grande, en el principio pedieremos 1 valor aleatorio, al final pediremos 100 valores aleatorios
    #como te explico que la lista variable, en el primer ciclo tendrá solo un valor random, pero en el último ciclo la lista tendrá 100 valores random
    #print("num vale{}, lista vale{}".format(num, lista_variable))
    times = 0
    lista_variable = grafiquitaDeInsertionSort(lista_variable) #por lo tanto debe recibir una lista
    print("este es times {}".format(times))
    eje_y.append(times) #no sé por qué pero times vale para cada ejecución diferente
    
print(lista_variable) #hasta aquí termina lo que se imprime digamos en la consola

#ax es una variable manta
fig, ax = plt.subplots(facecolor='c', edgecolor='b') #y es de yellow, c es cyan, m es magenta ,w es white, k es negro
ax.plot(eje_x, eje_y, marker="o", color="r", linestyle='None') #tal dotted, dashed, dashdot, bo hay mucha diferencia entre los tres
#r es de red, (por cierto b es de blue)
#en marker la o es de circle, * es e star, . point, , es pixel, hay muchos manta

ax.set_xlabel("x me dicen")
ax.set_ylabel("y sere")
ax.grid(True)  #grid significa como cuadrícula
ax.legend(["Soy Insertion Sort"])

plt.title("Me llaman Insertion sort")
plt.show() #aun no sé pa' que es esto



#plot significa trazo