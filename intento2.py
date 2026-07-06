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

#----------------- FUNCIONES 1, 2 y 3 MENU ------------------------------

def unidades_tipo(tipo, dicc_arreglos, dicc_bodega):

    cantDispo = 0

    for codigo, datos in dicc_arreglos.items():

        if tipo == datos[1]:
            cantDispo += dicc_bodega[codigo][1]

    print(f"----- Arreglo: {tipo} -----")
    print(f"El total de unidades disponibles es: {cantDispo}")
    print("")

def busqueda_precio(pmin, pmax, dicc_arreglos, dicc_bodega):

    lista = []

    for codigo, datos in dicc_bodega.items():

        if datos[0] >= pmin and datos[0] <= pmax and datos[1] > 0:
            producto = dicc_arreglos[codigo]
            lista.append(f"{producto[0]} -- {codigo}")

    if len(lista) == 0:
        print("No hay arreglos en ese rango de precios")
    else:
        lista.sort()

        for datos in lista:

            print(f"{datos}")

def buscar_codigo(codigo, dicc_arreglos):

    return codigo in dicc_arreglos

def actualizar_precio(codigo, nuevoprecio, dicc_arreglos, dicc_bodega):

    if buscar_codigo(codigo, dicc_arreglos):
        dicc_bodega[codigo][0] = nuevoprecio
        return True
    return False

#------------ FUNCION 4 VALIDACIONES TRUE O FALSE -------------------------

def validar_codigo(codigo, dicc_arreglos):

    if codigo.strip() == "":
        return False
    
    if codigo in dicc_arreglos:
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

#--------------- FUNCION AGREGAR ARREGLO ---------------------

def agregar_arreglo(dicc_arreglos, dicc_bodega):

    while True:
        codigo = input("Ingrese el codigo del arreglo: ").strip().upper()

        if validar_codigo(codigo, dicc_arreglos):
            break
        else:
            print("El codigo no puede estar repetido, vacio o tener espacios en blanco")

    while True:
        nombre = input("Ingrese el nombre: ").strip().title()

        if validar_nombre(nombre):
            break
        else:
            print("No puede quedar vacio ni tener espacios en blanco")

    while True:
        tipo = input("Ingrese tipo: ").strip().lower()

        if validar_tipo(tipo):
            break
        else:
            print("No puede quedar vacio ni tener espacios en blanco")

    while True:
        color = input("Ingrese color: ").strip().lower()

        if validar_color_principal(color):
            break
        else:
            print("No puede quedar vacio ni tener espacios en blanco")

    while True:
        tamano = input("Ingrese el tamaño (S, M, L): ").strip().upper()

        if validar_tamano(tamano):
            break
        else:
            print("Debe ser exactamente (S, M, L): ")

    while True:
        tarjetainp = input("Ingrese tarjeta (s-n): ").strip().lower()

        if validar_tarjeta(tarjetainp):
            tarjeta = True if tarjetainp == "s" else False
            break
        else:
            print("Debe ser (s-n)")

    while True:
        temporada = input("Ingrese temporada: ").strip().lower()

        if validar_temporada(temporada):
            break
        else:
            print("No puede quedar vacio ni tener espacios en blanco")

    while True:
        try:
            precio = input("Ingrese precio: ").strip()
            precio = int(precio)

            if validar_precio(precio):
                break
            else:
                print("Debe ser un numero entero mayor que 0")
        except ValueError:
            print("Debe ser un numero entero mayor que 0")

    while True:
        try:
            unidades = input("Ingrese unidades: ").strip()
            unidades = int(unidades)

            if validar_unidades(unidades):
                break
            else:
                print("Debe ser un numero entero mayor o igual que 0")
        except ValueError:
            print("Debe ser un numero entero mayor o igual que 0")

    dicc_arreglos[codigo] = [nombre, tipo, color, tamano, tarjeta, temporada]
    dicc_bodega[codigo] = [precio, unidades]
    print("--- ARREGLO AGREGADO EXITOSAMENTE ---")
    print("")

def eliminar_arreglo(codigo, dicc_arreglo, dicc_bodega):

    if buscar_codigo(codigo, dicc_arreglo):
        del dicc_arreglo[codigo]
        del dicc_bodega[codigo]
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

            tipoArreglo = input("Ingrese el tipo de arreglo: ").strip().lower()
            unidades_tipo(tipoArreglo, arreglos, bodega)

        case 2:

            while True:
                try:
                    precioMinimo = int(input("Ingrese el precio minimo: "))
                    precioMaximo = int(input("Ingrese el precio máximo: "))

                    if precioMinimo >= 0 and precioMaximo >= precioMinimo:
                        break
                    else:
                        print("El precio minimo debe ser menor al mayor")
                except ValueError:
                    print("ERROR: Debe ingresar valores enteros")

            print("---- ARREGLOS ENCONTRADOS ---- ")
            busqueda_precio(precioMinimo, precioMaximo, arreglos, bodega)
            print("")

        case 3:
            while True:
                codigobuscado = input("Ingrese el codigo del arreglo desea actualizar: ").strip().upper()

                while True:
                    try:
                        precio = int(input("Ingrese el nuevo valor: "))

                        if precio > 0:
                            break
                        else:
                            print("El valor debe ser mayor a 0")
                    except ValueError:
                        print("ERROR: debe ingresar un numero entero positivo")

                if actualizar_precio(codigobuscado, precio, arreglos, bodega):
                    print("--- NUEVO PRECIO ACTUALIZADO ---")
                    print("")
                else:
                    print("--- EL CODIGO NO EXISTE ---")
                    print("")

                seguir = input("Desea actualizar otro precio (s/n): ").strip().lower()

                if seguir == "n":
                    break
        
        case 4:
            agregar_arreglo(arreglos, bodega)

        case 5:
            eliminar = input("Ingrese el codigo del arreglo que desea eliminar: ").strip().upper()

            if eliminar_arreglo(eliminar, arreglos, bodega):
                print(f"--- Arreglo {eliminar} eliminado exitosamente ---")
                print("")
            else:
                print(f"--- No se encontro arreglo {eliminar} ---")
                print("")

        case 6:
            print("Programa finalizado")
            break
        case _:
            print("ERROR: opcion invalida debe ser entre (1-6)")