lista=[]
def fibonacci_inverso(): 
    #lista[1]=12 hoy descubrí que esto es incorrecto, no puedo agregar por el índice como lo soliamos hacer en arrays en C
    #lo malo de ello es que lista[index]= no solo me agregaba en cierto lugar sino también representa un elemento
    lista.insert(1, 12) #segun yo inserta en el índice 1
    return lista[0] #algo nuevo aprendido, los índices de las listas empiezan en 0, al igual que en un array en C

#en insert, si ya hay algo donde quieras insertar no te lo encima, te lo recorre a la siguiente posición(mayor)
print(fibonacci_inverso())
print(lista)
