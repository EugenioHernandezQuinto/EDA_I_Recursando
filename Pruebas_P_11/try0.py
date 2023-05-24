#mi intención es evitar listas, y así no tener que poner lo que puso este manto para quitar las llaves, y evitar hacerla de cadenas. Y en lugar de usar (::1) para regresar la lista al reves mejor usar ingenio. Aunque esto implique quitar los casos bases...?
#lo que pasa es que yo no siento que esos sean casos base, al menos de lo que voy entendiendo que es un caso base, lo que quiero es hacerlo al menos más explícito, aunque no creo que lo logre
#no quiero global :c
lista=[]
def fibonacci_inverso(n): #usaremos una lista, pa' honrar el trabajo anterior
    if (n - 1) <= 1:
        lista.insert(0,n-1) #en el index 0 va a poner número de elemento menos 1
        return lista[0] #solo aplica para los default de la serie que son 0 y 1
    #no necesitamos un else 
    #print(fibonacci_inverso(n-1)) #perdoname compu
    #print(fibonacci_inverso(n-2))
    temp=fibonacci_inverso(n-1) + fibonacci_inverso(n-2)
    print(temp)
    lista.insert(0, temp)#no sé si es lo mismo ese 0 que n
    return temp
    #return fibonacci_inverso(n-1)+fibonacci_inverso(n-2) si solo pones esto solo vas a poder regresar el más grande bro, creo.
#para conseguir que regersae en orden invesro necesita devolver la instrucción
#la verdad que para que nos de del mayor al menor es hacer más isntrucciones al chile, 
#hay que tener en cuenta que si regresa algo al main, va a salirse de la función, por eso sho digo que mejor si lo pongas en una función

#quiero 8 elementos
#comprobar que no sea 0, por que de otra manera quiere 0 elementos, no quiere nada
#insertar el 1 significa imprimir 0


fibonacci_inverso(8)
print(lista)

    