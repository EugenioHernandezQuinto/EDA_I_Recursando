contador=0

inventario = {}
inventario['gelatina'] = 'dgari'
inventario['leche'] = 'santa'
inventario['papel'] = 'petalos'
inventario['tortillas'] = 'noBrand'
inventario['lumus'] = 'laCosteña'


def ordenar_por_nombre(item):
    return item[1] 

def ordenar_por_codigo(item): 
    print("Entré 2\n")
    print("Averiguando qué es item {}\n".format(item))
    print("item[0] es {}\n".format(item[0]))
    return item[0]

def ordenar_suministros(criterio):
    global contador
    listaDeTuplas_Diccionario = list(inventario.items()) 

    if criterio == 'nombre':
        contador+=1
        print("Antes, funcion ordenadr_suministros() {}".format(contador))
        listaDeTuplas_Diccionario = merge_sort(listaDeTuplas_Diccionario, ordenar_por_nombre)
        contador+=1
        print("Después, funcion ordenadr_suministros() {}".format(contador))
        #print("soy una lista que solo debe contener nombres(items) {}".format(listaDeDiccionario)) #esta función no conoce key
    elif criterio == 'codigo':
        listaDeTuplas_Diccionario = merge_sort(listaDeTuplas_Diccionario, ordenar_por_codigo) 
        
    #print(listaDeTuplas_Diccionario)#imprime una lista,[], de tuplas,().
    return listaDeTuplas_Diccionario #sabemos que al fianl regresa una lista de tuplas, pero la envúa muy raro. Por que listasDeDiccionario ya es una lista de tuplas

def merge_sort(listaDeTuplas_Diccionario, key): 
    if len(listaDeTuplas_Diccionario) <= 1: 
        return listaDeTuplas_Diccionario
    else:
        middle = len(listaDeTuplas_Diccionario) // 2
        left = listaDeTuplas_Diccionario[ : middle] #is kinda understandable, es como [middle] i think, is like one before middle
        right = listaDeTuplas_Diccionario[middle : ]
        left = merge_sort(left, key)#aquí digamos que utiliza key por primera vez en algun la primera vez, pero te das cuenta que esta función tampoco conoce key
        right = merge_sort(right, key)
        return merge(left, right, key)

def merge(left, right, key): #key representa nombres
    result = [] #soy una lista manta
    i = j = 0
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            print("qué es key {}".format(   key(left[i]))  )
            result.append(left[i])
            i += 1
        else:
            print("qué es key {}".format(   key(right[i]))  )
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

#////////////////////////////////////////////////////////////////
#criterio = 'codigo'
criterio = 'nombre'
ordenados = ordenar_suministros(criterio)
print("\n\n")

for codigo, nombre in ordenados:
    print(f'{codigo} - {nombre}')
