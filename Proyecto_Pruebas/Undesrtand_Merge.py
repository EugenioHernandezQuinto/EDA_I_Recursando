inventario = {}

def ordenar_por_nombre(articulo):
    return articulo[1]

def ordenar_por_codigo(articulo):
    return articulo[0]

def ordenar_suministros(criterio):

    articulos = list(inventario.items()) #inventario es un diccionario
    #creo que convierte en lista algo, no sé exactamente qué

    if criterio == 'nombre':
        articulos = merge_sort(articulos, key = ordenar_por_nombre) #key significa que ha de haber varias

    elif criterio == 'codigo':
        articulos = merge_sort(articulos, key = ordenar_por_codigo) #mira key podia ser declarada fuera, pero destalles.
    
    return [(k, v) for k, v in items] #must be a list, because of it[]

def merge_sort(items, key): #i should undestand it but kinda refuse
    if len(items) <= 1:
        return items
    else:
        middle = len(items) // 2
        left = items[:middle] #is kinda understandable, es como [middle] i think, is like one before middle
        right = items[middle:]
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
criterio = input('Ingresa en minúsculas y sin acentos el criterio de orden (nombre o codigo): ')
ordenados = ordenar_suministros(criterio)
        
for codigo, nombre in ordenados:
    print(f'{codigo} - {nombre}')
