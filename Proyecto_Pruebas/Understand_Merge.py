inventario = {}
inventario['gelatina'] = 'dgari'
inventario['leche'] = 'santa'
inventario['papel'] = 'petalos'
inventario['tortillas'] = 'noBrand'
inventario['lumus'] = 'laCosteña'


def ordenar_por_nombre(item):
    print("Entré 1\n")
    print("Averiguando qué es item {}\n".format(item))#item es una lista: ('gelatina' , 'dgari')
    print("item[1] es {}\n".format(item[1])) #como carajos sabe qué es item?
    return item[1] #articulos realmente se refiere a algun item #item[1] es dgari es el nombre/item, creo que lo que devuelve es tipo string

def ordenar_por_codigo(item): #ya sé que pez, muy raro
    print("Entré 2\n")
    print("Averiguando qué es item {}\n".format(item))
    print("item[0] es {}\n".format(item[0]))
    return item[0]

def ordenar_suministros(criterio):

    listasDeDiccionario = list(inventario.items()) #inventario es un diccionario
    #print("dime qué soy ahora, creo que lista {}".format(listasDeDiccionario)) #es una lista de tuplas
    #imprime esto [('gelatina', 'dgari'), ('leche', 'santa'), ('papel', 'petalos'), ('tortillas', 'noBrand'), ('lumus', 'laCosteña')]


    if criterio == 'nombre':
        listasDeDiccionario = merge_sort(listasDeDiccionario, ordenar_por_nombre) #key significa que ha de haber varias
        #lo que queremos es crear una lista con solo nombres(items)
        #de cualquier forma, lo que devuelva ordenar_por_nombre lo pone en key. Cueiosamente, siento que no ejecuta prmero ordenar_por_nombre, sino merge_sort
        print("soy una lista que solo debe contener nombres(items) {}".format(listasDeDiccionario)) #esta función no conoce key
    elif criterio == 'codigo':
        listasDeDiccionario = merge_sort(listasDeDiccionario, ordenar_por_codigo) #mira key podia ser declarada fuera, pero destalles.
        #lo que queremos es crear una lista con solo codigos(keys)
        print("soy una lista que solo debe contener codigos(keys) {}".format(listasDeDiccionario))
    return [(k, v) for k, v in listasDeDiccionario] #must be a list, because of it[]

def merge_sort(items, key): #i should undestand it but kinda refuse
    if len(items) <= 1:
        return items
    else:
        middle = len(items) // 2
        left = items[: middle] #is kinda understandable, es como [middle] i think, is like one before middle
        right = items[middle :]
        left = merge_sort(left, key)
        right = merge_sort(right, key)
        return merge(left, right, key)

def merge(left, right, key):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

#////////////////////////////////////////////////////////////////
#criterio = 'codigo'
criterio = 'nombre'
ordenados = ordenar_suministros(criterio) #segun yo es una lista de tuplas
print("\n\n")

for codigo, nombre in ordenados:
    print(f'{codigo} - {nombre}')
#también se puede imprimir el diccionario en sí con print(diccionario), pero supongo que es presentación
#hasta el momento confiamos en que el usuario nos dé algo válido como orden
