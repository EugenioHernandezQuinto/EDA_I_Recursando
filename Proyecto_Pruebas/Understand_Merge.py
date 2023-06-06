inventario = {}
inventario['gelatina'] = 'dgari'
inventario['leche'] = 'santa'
inventario['papel'] = 'petalos'
inventario['tortillas'] = 'noBrand'
inventario['lumus'] = 'laCosteña'


def ordenar_por_nombre(item):
    print("Entré 1")
    print("item[1] es {}".format(item[1])) #como carajos sabe qué es item?
    return item[1] #articulos realmente se refiere a algun item

def ordenar_por_codigo(item):
    print("Entré 2")
    print("item[0] es {}".format(item[0]))
    return item[0]

def ordenar_suministros(criterio):

    items = list(inventario.items()) #inventario es un diccionario
    print("dime qué soy ahora, creo que lista {}".format(items)) #ha de ser una lista de solo los items, sin kesy pues
    #creo que convierte en lista algo, no sé exactamente qué

    if criterio == 'nombre':
        items = merge_sort(items, key = ordenar_por_nombre) #key significa que ha de haber varias

    elif criterio == 'codigo':
        items = merge_sort(items, key = ordenar_por_codigo) #mira key podia ser declarada fuera, pero destalles.
    
    return [(k, v) for k, v in items] #must be a list, because of it[]

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
#criterio = 'coddigo'
criterio = 'nombre'
ordenados = ordenar_suministros(criterio)

print("\n\n")
for codigo, nombre in ordenados:
    print(f'{codigo} - {nombre}')
#también se puede imprimir el diccionario en sí con print(diccionario), pero supongo que es presentación
