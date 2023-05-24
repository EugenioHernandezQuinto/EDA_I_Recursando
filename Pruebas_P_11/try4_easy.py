#me lo robé del profe
def recur_fibo(n):
    if n<=1: 
        return n
    else:
        return(recur_fibo(n-1))+ recur_fibo(n-2)  #lo primero que regresa es cero

nterms=13
lista=[]

if nterms<=0: #significa que no quiere ningún elemento
    print("Por favor ingrese un número entero positivo.")
else:
    print("Secuencia Fibonacci")
    for i in range(nterms): #a caray, por que estamos en una iteración
       lista.insert(0, recur_fibo(i)) #te va regresando el elemento más pequeño

print(lista)