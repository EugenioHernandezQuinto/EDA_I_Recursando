#mi intención es evitar listas, y así no tener que poner lo que puso este manto para quitar las llaves, y evitar hacerla de cadenas. Y en lugar de usar (::1) para regresar la lista al reves mejor usar ingenio. Aunque esto implique quitar los casos bases...?
#lo que pasa es que yo no siento que esos sean casos base, al menos de lo que voy entendiendo que es un caso base, lo que quiero es hacerlo al menos más explícito, aunque no creo que lo logre

def fibonacci_inverso(n): #trabajamos con listas
                          #no usamos recursión
    if n <= 0: #basicamente dice: quiero 0 elementos de la serie de Fibonacci, aunque aquí se le agregó para cuando da un número negativo, ñe
        return []
    elif n == 1: #quiero 1 elemento de la serie de Fibonacci
        return [0]
    elif n == 2: #quiero 2 elementos de la serie de Fibonacci
        return [1, 0] #en caso de que quiera ver dos elementos, dejamos una lista que ya esta en el orden especificado en la practica
    else: #quiero más de 2 elementos de la serie de fibonacci
        fib = [0, 1] 
        for i in range(n-2):#empieza en cero y no toca el n-2
            #print(i)
            #print("Hola {}".format(fib[-1]))#es curioso como las tratamos como la estructura array in C, lo que pasa es que las listas tienene index
            #print("Adiós {}".format(fib[-2]))
            fib.append(fib[-1] + fib[-2]) #esta parte lo que hace es tomar los dos últimos elementos y sumarlos, sin embargo no sabemos que tanto se nos va a extender la lista, así que una forma inteligente de averiguar cuales son los dos últimos elementos es usar índices nengativos, 
        return fib[::-1] #al parecer es para regresar la lista al revés
        #es para invertir la lista, hay otras formas además de esta, como la función reverse() o reversed() quién sabe

if __name__ == '__main__':
    print('Bienvenido, puede realizar las siguientes operaciones:\n')
    print('1 Serie de Fibonacci\n')
    print('2 Salir\n')
    opcion = int(input('Ingrese la opcion: '))

    if opcion == 1:
        n = int(input('Ingrese el número entero N: '))#regresa N numeros de la serie de Fibonacci
        print(fibonacci_inverso(n)) #curioso es ue solo se manda a llamar una vez
    elif opcion == 2:
        exit()
    