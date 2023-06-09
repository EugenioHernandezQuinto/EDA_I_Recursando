#merge
inventario = {} # Diccionario para almacenar el inventario de suministros
clientes = [] # Lista para almacenar las quejas de los clientes
trabajadores = {} # Diccionario para almacenar información de los trabajadores

def agregar_suministros(codigo, nombre):
    # Agrega un artículo al inventario con el código y nombre dados
    inventario[codigo] = nombre

def quitar_suministros(codigo):
    # Elimina un artículo del inventario con el código dado
    if codigo in inventario:
        inventario[codigo] = None

def ordenar_por_nombre(item):
    # Función clave para ordenar por nombre
    return item[1]

def ordenar_por_codigo(item):
    # Función clave para ordenar por código
    return item[0]

def ordenar_suministros(criterio):
    # Ordena los artículos del inventario según el criterio dado (nombre o código)
    items = list(inventario.items())
    
    if criterio == 'nombre':
        # Ordenar por nombre usando merge sort
        items = merge_sort(items, key=ordenar_por_nombre)
    elif criterio == 'codigo':
        # Ordenar por código usando merge sort
        items = merge_sort(items, key=ordenar_por_codigo)
    
    return [(k, v) for k, v in items]

def merge_sort(items, key):
    # Implementación del algoritmo merge sort
    if len(items) <= 1:
        return items
    else:
        middle = len(items) // 2
        left = items[:middle]
        right = items[middle:]
        left = merge_sort(left, key)
        right = merge_sort(right, key)
        return merge(left, right, key)

def merge(left, right, key):
    # Función auxiliar para mezclar dos listas ordenadas
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
    # Calcula el costo total de la lista de productos dada
    total = 0
    for codigo in lista_productos:
        total += inventario[codigo]['precio']
    return total

def atencion_clientes(codigo_producto, mensaje):
    global clientes
    # Agrega una queja de cliente a la lista de clientes
    clientes += [{'codigo_producto': codigo_producto, 'mensaje': mensaje}]

#-------------------------------------------------------------------

def alta_trabajador(codigo, nombre, apellido, puesto):
    # Agrega un trabajador a la lista de trabajadores con el código, nombre, apellido y puesto dados
    trabajadores[codigo] = {'nombre': nombre, 'apellido': apellido, 'puesto': puesto}

def baja_trabajador(codigo):
    # Elimina un trabajador de la lista de trabajadores con el código dado
    if codigo in trabajadores:
        trabajadores[codigo] = None

def cambio_puesto(codigo, nuevo_puesto):
    # Cambia el puesto de un trabajador con el código dado al nuevo puesto
    trabajadores[codigo]['puesto'] = nuevo_puesto

#****************************************************************
#detalles pero ¿por qué no poner el menú abajo?
def menu():
    # Muestra el menú principal
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

#*****************************************************

def menu_inventario():
    # Muestra el menú de administración de inventario
    print('---Administración de Inventario---')
    print('Menú:')
    print('1. Agregar suministros')
    print('2. Quitar suministros')
    print('3. Ordenar suministros')
    
    opcion = input('Selecciona una opción: ')
    
    if opcion == '1':
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
    # Muestra el menú de clientes
    print('---Atención a clientes---')
    print('Menú:')
    print('1. Cobro de productos')
    print('2. Atención a problemas')
    
    opcion = input('Selecciona una opción: ')
    
    if opcion == '1':
        lista_productos = [] #es una lista vacía
        
        while True:
            codigo = input('\nAgrega los productos a tu lista (deja en blanco para terminar): ')
            
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
    # Muestra el menú del personal
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

menu()

#aun no hay forma de regresar al menú principal
#hay que ver si los códigos son números
#hay que pedir la entrada de orden en minúsculas y sin acentos