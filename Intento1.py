#---------------------- Funcion menu y leer opcion --------------------
def menu():

    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por tipo de arreglo")
    print("2. Búsqueda de arreglos por rango de precio")
    print("3. Actualizar precio de arreglo")
    print("4. Agregar arreglo")
    print("5. Eliminar arreglo")
    print("6. Salir")
    print("=====================================")

def leer_opcion():

    while True:
        try:
            opcion = int(input("Ingrese una opcion del menu: "))
            return opcion
        except ValueError:
            print("Debe seleccionar una opcion valida")

#---------------------------- Funciones opciones---------------------

def unidades_tipo(tipo, dicc_arreglos, dicc_bodega):

    cantDispo = 0

    for codigo, datos in dicc_arreglos.items():

       if tipo == datos[1]:
           producto = dicc_bodega[codigo]
           cantDispo += producto[1]

    print(f"---- Arreglo tipo {tipo} ----")
    print(f"El total de unidades disponible son: {cantDispo}")
    print("")

def busqueda_precio(p_min, p_max, dicc_arreglos, dicc_bodega):

    lista = []

    for codigo, datos in dicc_bodega.items():

        if datos[0] >= p_min and datos[0] <= p_max and datos[1] > 0:
            producto = dicc_arreglos[codigo]
            lista.append(producto[0] + "---" + codigo)

    if len(lista) == 0:
        print("No hay arreglos en ese rango de precio")
    else:
        lista.sort()

        for arreglos in lista:

            print(f"Los arreglos encontrados son: {arreglos}")

def buscar_codigo(codigo, dicc_arreglos):
    
    return codigo in dicc_arreglos

def actualizar_precio(codigo, nuevo_precio, dicc_arreglos, dicc_bodega):

    if buscar_codigo(codigo, dicc_arreglos):
        dicc_bodega[codigo][0] = nuevo_precio
        return True
    return False

def validar_codigo(codigo, dicc_bodega):

    if codigo.strip() == "":
        return False
    
    if codigo in dicc_bodega:
        return False
    
    return True

def validar_nombre(nombre):

    if nombre.strip() == "":
        return False
    return True

def validar_tipo(tipo):

    if tipo.strip() == "":
        return False
    return True

def validar_color_principal(color):

    if color.strip() == "":
        return False
    return True

def validar_tamano(tamano):

    return tamano.upper() in ["S", "M", "L"]

def validar_tarjeta(tarjeta):

  return tarjeta.lower() in ["s", "n"]

def validar_temporada(temporada):

    if temporada.strip() == "":
        return False
    return True

def validar_precio(precio):

    if precio > 0:
        return True
    return False

def validar_unidades(unidades):

    if unidades >= 0:
        return True
    return False

def agregar_arreglo(dicc_arreglos, dicc_bodega):

    while True:
        codigo = input("Ingrese codigo del arreglo: ").strip().upper()

        if validar_codigo(codigo, dicc_bodega):
            break
        else:
            print("No debe estar vacio, tener espacios ni estar repetido")

    while True:
        nombre = input("Ingrese nombre: ").strip().title()

        if validar_nombre(nombre):
            break
        else:
            print("No debe quedar vacio ni tener espacios en blanco")

    while True:
        tipo = input("Ingrese tipo: ").strip().lower()
        
        if validar_tipo(tipo):
            break
        else:
            print("No debe quedar vacio ni tener espacios en blanco")

    while True:
        color = input("Ingrese color: ").strip().lower()

        if validar_color_principal(color):
            break
        else:
            print("No debe quedar vacio ni tener espacios en blanco")

    while True:
        tamano = input("Ingrese tamaño (S,M,L): ").strip().upper()

        if validar_tamano(tamano):
            break
        else:
            print("Debe ser (S,M,L)")

    while True:
        tarjetainp = input("Ingrese tarjeta (s-n): ").strip().lower()

        if validar_tarjeta(tarjetainp):
            tarjeta = True if tarjetainp == "s" else False
            break
        else:
            print("Debe ser (s-n)")

    while True:
        temporada = input("Ingrese temporada: ")

        if validar_temporada(temporada):
            break
        else:
            print("No debe quedar vacio ni tener espacios en blanco")

    while True:
        try:
            precio = input("Ingrese precio: ").strip()

            precio = int(precio)

            if validar_precio(precio):
                break
            else:
                print("Debe ser un numero mayor que 0")
        except ValueError:
            print("Debe ser un numero mayor que 0")

    while True:
        try:
            unidades = input("Ingrese unidades: ").strip()

            unidades = int(unidades)

            if validar_unidades(unidades):
                break
            else:
                print("Debe ser mayor o igual a 0")
        except ValueError:
            print("Debe ser mayor o igual a 0")

    dicc_arreglos[codigo] = [nombre, tipo, color, tamano, tarjeta, temporada]
    dicc_bodega[codigo] = [precio, unidades]
    print("--- PRODUCTO AGREGADO EXITOSAMENTE ---")
    print("")
        

def eliminar_arreglo(codigo, dicc_arreglos, dicc_bodega):

    if buscar_codigo(codigo, dicc_arreglos):
        del dicc_bodega[codigo]
        del dicc_arreglos[codigo]
        return True
    return False
    

arreglos = {
    'FLO1': ['Ramo Primavera', 'ramo', 'rosado', 'M', True,'primavera'],
    'FLO2': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todo año'],
    'FLO3': ['Ramo Solar', 'ramo', 'amarillo', 'S', False, 'verano'],
    'FLO4': ['Centro Mesa', 'centro', 'rojo', 'M', True, 'todo año'],
    'FLO5': ['Ramo Bosque', 'ramo', 'verde', 'L', False, 'otoño'],
    'FLO6': ['Caja Noche', 'caja', 'morado', 'M', True, 'invierno'],
}

bodega = {
    'FLO1': [15990, 8],
    'FLO2': [29990, 3],
    'FLO3': [9990, 12],
    'FLO4': [24990, 5],
    'FLO5': [19990, 0],
    'FLO6': [22990, 6],
}

while True:

    menu()
    opcionMenu = leer_opcion()

    match opcionMenu:

        case 1:
            tipoArreglo = input("Ingrese el tipo de arreglo que desea buscar: ").strip().lower()
            unidades_tipo(tipoArreglo, arreglos, bodega)

        case 2:

            while True:
                try:
                    precioMinimo = int(input("Ingrese precio minimo: "))
                    precioMaximo = int(input("Ingrese precio máximo: "))

                    if precioMinimo >= 0 and precioMaximo >= precioMinimo:
                        break
                    else:
                        print("ERROR, el precio minimo debe ser menor al máximo")
                except ValueError:
                    print("ERROR, debe ingresar valores enteros")

            print("---- ARREGLOS EN RANGO DE PRECIO ---- ")
            busqueda_precio(precioMinimo, precioMaximo, arreglos, bodega)
            print("")

        case 3:
            
            while True:
               
                codigoArreglo = input("Ingrese el codigo del arreglo: ").strip().upper()

                while True:
                    try:
                        precio = int(input("Ingrese el precio actualizado: "))

                        if precio > 0:
                            break
                        else:
                            print("El precio debe ser entero positivo ")
                    except ValueError:
                        print("Error: debe ingresar un numero entero")

                if actualizar_precio(codigoArreglo, precio, arreglos, bodega):
                    print("--- PRECIO ACTUALIZADO ---")
                    print("")
                else:
                    print("--- NO SE PUDO ACTUALIZAR ---")
                    print("")

                pregunta = input("¿Desea actualizar otro precio? (s/n): ").strip().lower()

                if pregunta == "n":
                    break
        
        case 4:
            agregar_arreglo(arreglos, bodega)

        case 5: 
            codigoEliminar = input("Ingrese el codigo a eliminar: ").strip().upper()

            if eliminar_arreglo(codigoEliminar, arreglos, bodega):
                print("")
                print(f"--- ARREGLO {codigoEliminar} ELIMINADO ---")
            else:
                print(f"--- CODIGO {codigoEliminar} NO EXISTE ---")
                print("")

        case 6:
            print("Programa finalizado.")
            break
        case _:
            print("ERROR: debe ser opcion entre (1-6)")



        