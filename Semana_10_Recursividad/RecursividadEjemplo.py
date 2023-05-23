#Un programa en C para demostrar el funcionamiento de la recursividad.
#i=0

def printFun(test):
    #global i #brother no sé como funciona esta cosa, no sé python
    #i=i+1
    if test < 1:
        return
    else:
        print(test)
        printFun(test - 1) #sentencia 2
        #print("i es {}".format(i))
        return

#Función principal
if __name__=='__main__':
    test = 3
    printFun(test)