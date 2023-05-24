memoria={1:0, 2:1, 3:1} 

def fibonacci_memo(numero):
    if numero in memoria: 
        return memoria[numero] 
    memoria[numero]=fibonacci_memo(numero-1) + fibonacci_memo(numero-2) 
    return memoria[numero]

print(fibonacci_memo(13))
print(memoria)