#merge
inventario = {} #this ones are gonna be kinda difficult to understand
clientes = [] 
trabajadores = {} 



def agregar_suministros(codigo, nombre):
    inventario[codigo] = nombre

def quitar_suministros(codigo):
    if codigo in inventario:
        inventario[codigo] = None

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
    
#------------------------------------------------------------------

def cobro_productos(lista_productos):
    total = 0
    for codigo in lista_productos:
total += inventario[codigo]['p recio']
    return total

def atencion_clientes(codigo_producto, mensaje):
    global clientes
    clientes += [{'codigo_producto': codigo_producto, 'mensaje': mensaje}]

#-------------------------------------------------------------------

def alta_trabajador(codigo, nombre, apellido, puesto):
    trabajadores[codigo] = {'nombre': nombre, 'apellido': apellido, 'puesto': puesto}

def baja_trabajador(codigo):
    if codigo in trabajadores:
        trabajadores[codigo] = None

def cambio_puesto(codigo, nuevo_puesto):
    trabajadores[codigo]['puesto'] = nuevo_puesto

#****************************************************************

def menu_inventario():
    print('---Administración de Inventario---')
    print('Menú:')
    print('1. Agregar suministros')
    print('2. Quitar suministros')
    print('3. Ordenar suministros')
    
    opcion = input('Selecciona una opción: ')
    
    if opcion == '1':
        #¿ qué tendrá que decir tipo de suminstro?
        codigo = input('Ingresa el código del suministro: ')
        nombre = input('Ingresa el nombre del suministro: ')
        agregar_suministros(codigo, nombre)
        print('\nSuministro agregado\n')
        menu_inventario()
        
    elif opcion == '2':
        codigo = input('Ingresa el código del suministro: ')
        quitar_suministros(codigo)
        print('\nSuministro quitado\n')
        menu_inventario()
        
    elif opcion == '3':
        criterio = input('Ingresa el criterio de orden (nombre o codigo): ')
        ordenados = ordenar_suministros(criterio)
        
        for codigo, nombre in ordenados:
            print(f'{codigo} - {nombre}')
        
        menu_inventario()

#*****************************************************

def menu_clientes():
    print('---Atención a clientes---')
    print('Menú:')
    print('1. Cobro de productos')
    print('2. Atención a problemas')
    
    opcion = input('Selecciona una opción: ')
    
    if opcion == '1':
        lista_productos = [] #es una lista vacía
        
        while True:
            codigo = input('\nAgrega los productos a tu lista (deja en blanco para terminar): ')
            #sería bueno imprimir qué productos existen
            if codigo == '':
                break #rompe el ciclo while
            
            lista_productos += [codigo]
        
        total = cobro_productos(lista_productos) #devuelve una tupla #ha de devolver un ticket
        
        print(f'\nSu total es de: ${total}\n') #es una tupla
        
        menu_clientes()
        
    elif opcion == '2':
        codigo_producto = input('\nIngresa el código del producto: ')
        mensaje = input('\nIngresa tu queja o problema: ')
        
        atencion_clientes(codigo_producto, mensaje)
        
        print('\nQueja registrada\n')
        
        menu_clientes()

#*****************************************************

def menu_personal():
    print('---Administración de Personal---')
    print('Menú:')
    print('1. Altas')
    print('2. Bajas')
    print('3. Cambios de puesto')

    opcion = input('\nSelecciona una opción: ')

    if opcion == '1':
        codigo = input('\nIngresa el código del trabajador: ')
        nombre = input('\nIngresa el nombre del trabajador: ')
        apellido = input('\nIngresa el apellido del trabajador: ')
        puesto = input('\nIngresa el puesto del trabajador: ')

        alta_trabajador(codigo, nombre, apellido, puesto)

        print('\nTrabajador dado de alta\n')

        menu_personal()

    elif opcion == '2':
        codigo = input('\nIngresa el código del trabajador: ')
        #falta darlo de baja por su nombre

        baja_trabajador(codigo)

        print('\nTrabajador dado de baja\n')

        menu_personal()

    elif opcion == '3':
        codigo = input('\nIngresa el código del trabajador: ')
        nuevo_puesto = input('\nIngresa el nuevo puesto del trabajador: ')

        cambio_puesto(codigo, nuevo_puesto)

        print('\nCambio realizado\n')

        menu_personal()

#*************************************************************

#detalles pero ¿por qué no poner el menú abajo?
def menu():
    print('---Sistema de Administración de Puma Abarrotero S.A. de C.V.---')
    print('Menú:')
    print('1. Administración de Inventario')
    print('2. Atención a Clientes')
    print('3. Administración de Personal')
    
    opcion = input('Selecciona una opción: ')
    
    if opcion == '1':
        menu_inventario()
    elif opcion == '2':
        menu_clientes()
    elif opcion == '3':
        menu_personal()

menu()
