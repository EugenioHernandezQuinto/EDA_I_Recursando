# Ejemplo de Serie de Fibonacci
# Función Fibonacci

def fib(n):
    # Caso base 1
    if n == 0:
        return 0

    # Caso base 2
    if n == 1 or n == 2:
        return 1

    # Llamada recursiva
    else:
        return (fib(n - 1) + fib(n - 2))

#Función Main
if __name__=='__main__':
    # Iniciando variable n.
    n = 5
    print("Resultado de la entrada {} ".format(n))
    
    # Ciclo para imprimir la serie.
    for i in range(0,n): #según yo no toca n #era lo mismo in range(n)
        print(fib(i)) #Inicio de llamada