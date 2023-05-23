def imprimir(n):
    if n < 0:
        return 
    print(n)

    # La última instrucción ejecutada es una llamada recursiva.
    imprimir(n-1)

#se llama recursion en cola por que la última instrucción es la cola

imprimir(9)