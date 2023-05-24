lista=[]
def fibonacci_inverso(n):
    if n <= 1: #no va a aplicar cuando el usuario quiere 3 elementos, por que ya no podria ser igual a n
        lista.insert(0, n)
        return lista[n]
        #sabemos que append los inserta al último
        #un insert(0, etc) va a insertar siempre al incio
        #haber usado el de memo la verdad nos hubiera dado muchas vueltas, ni yo se porque, luego me explicas también a mi por que 
    #else pensemos
    lista.insert(n, fibonacci_inverso(n-1)+fibonacci_inverso(n-2))
    return lista[n]

n=8 #me lo da el usuario
#verificamos que no sea cero 
n=n-1 #de esta manera los elementos de la lista se pueden guardar desde el primer índice(las listas tienen índices que empiezan desde 0)
#aunque luego me avisas si podía evitar esto

fibonacci_inverso(n)
print(lista)

#si las cosas no te funcionan solo ponle un insert en 0 al de lab del viernes