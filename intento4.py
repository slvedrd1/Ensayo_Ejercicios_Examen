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

            if opcion > 0 and opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opcion valida")
        except ValueError:
            print("Debe seleccionar una opcion valida")

#-------------------FUNCIONES OPCION 1, 2 Y 3 ----------------------

def unidades_tipo(tipo, dicc_arreglos, dicc_bodega):

    cantDispo = 0

    for codigo, datos in dicc_arreglos.items():

        if tipo == datos[1]:
            cantDispo += dicc_bodega[codigo][1]

    print(f"--- Arreglo {tipo} ---")
    print(f"Unidades: {cantDispo}")
    print("")

def busqueda_precio(p_min, p_max, dicc_arreglos, dicc_bodega):

    lista = []

    for codigo, datos in dicc_bodega.items():

        if datos[0] >= p_min and datos[0] <= p_max and datos[1] > 0:
            producto = dicc_arreglos[codigo][0]
            lista.append(f"{producto} -- {codigo}")

    if len(lista) == 0:
        print("No hay arreglos en ese rango de precios.")
    else:
        lista.sort()

        print("--- Arreglos disponibles en rango de precio ---")
        for datos in lista:

            print(f"{datos}")
        print("")

def buscar_codigo(codigo, dicc_arreglos):
    
    return codigo in dicc_arreglos

def actualizar_precio(codigo, precio, dicc_arreglos, dicc_bodega):

    if buscar_codigo(codigo, dicc_arreglos):
        dicc_bodega[codigo][0] = precio
        return True
    return False

#--------------- def validaciones agregar ---------------------------

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

def validar_color(color):

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

#------------------------------- FUNCION 4 AGREGAR -----------------------

def agregar_arreglo(dicc_arreglos, dicc_bodega):

    while True:
        codigo = input("Ingrese codigo del arreglo: ").strip().upper()

        if validar_codigo(codigo, dicc_arreglos):
            break
        else:
            print("No debe quedar vacio ni ya existir previamente.")

    while True:
        nombre = input("Ingrese nombre: ").strip().title()

        if validar_nombre(nombre):
            break
        else:
            print("No debe quedar vacio.")

    while True:
        tipo = input("Ingrese tipo: ").strip().lower()

        if validar_tipo(tipo):
            break
        else:
            print("No debe quedar vacio.")

    while True:
        color = input("Ingrese color: ").strip().lower()

        if validar_color(color):
            break
        else:
            print("No debe quedar vacio.")

    while True:
        tamano = input("Ingrese tamaño (S/M/L): ").strip().upper()

        if validar_tamano(tamano):
            break
        else:
            print("Debe ser (S/M/L).")

    while True:
        tarjeta = input("Ingrese tarjeta (s/n): ").strip().lower()

        if validar_tarjeta(tarjeta):
            tarjetabool = True if tarjeta == "s" else False
            break
        else:
            print("Debe ser (s/n).")

    while True:
        temporada = input("Ingrese temporada: ").strip().lower()

        if validar_temporada(temporada):
            break
        else:
            print("No debe quedar vacio.")

    while True:
        try:
            precio = input("Ingrese precio: ").strip()
            precio = int(precio)

            if validar_precio(precio):
                break
            else:
                print("Debe ser un entero positivo.")
        except ValueError:
            print("Debe ser un entero positivo.")

    while True:
        try:
            unidades = input("Ingrese unidades: ").strip()
            unidades = int(unidades)

            if validar_unidades(unidades):
                break
            else:
                print("Debe ser un entero positivo.")
        except ValueError:
            print("Debe ser un entero positivo.")

    dicc_arreglos[codigo] = [nombre, tipo, color, tamano, tarjetabool, temporada]
    dicc_bodega[codigo] = [precio, unidades]
    print("--- ARREGLO AGREGADO ---")
    print("")

def eliminar_arreglo(codigo, dicc_arreglos, dicc_bodega):

    if buscar_codigo(codigo, dicc_arreglos):
        del dicc_arreglos[codigo]
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

            buscarTipo = input("Ingrese tipo a buscar: ").strip().lower()
            unidades_tipo(buscarTipo, arreglos, bodega)

        case 2:

            while True:
                try:
                    pmin = int(input("Ingrese precio minimo: "))
                    pmax = int(input("Ingrese precio maximo: "))
                    
                    if pmin >= 0 and pmax >= pmin:
                        break
                    else:
                        print("El precio minimo no debe ser mayor que el maximo.")
                except ValueError:
                    print("El valor debe ser un numero entero positivo")

            busqueda_precio(pmin, pmax, arreglos, bodega)

        case 3:

            while True:
                
                codigo = input("Ingrese codigo del arreglo: ").strip().upper()

                while True:
                    try:
                        nuevoPrecio = int(input("Ingrese nuevo precio: "))

                        if nuevoPrecio > 0:
                            break
                        else:
                            print("El valor debe ser entero positivo")
                    except ValueError:
                        print("El valor debe ser entero positivo")

                if actualizar_precio(codigo, nuevoPrecio, arreglos,bodega):
                    print("--- PRECIO ACTUALIZADO ---")
                    print("")
                else:
                    print("--- EL CODIGO NO EXISTE ---")
                    print("")

                while True:

                    seguir = input("Desea actualizar otro precio (s/n): ").strip().lower()

                    if seguir == "s":
                        break
                    elif seguir == "n":
                        break
                    else:
                        print("Opcion invalida debe ser (s/n).")

                if seguir == "n":
                    break

        case 4:
            agregar_arreglo(arreglos, bodega)

        case 5:
            eliminar = input("Ingrese codigo que desea eliminar: ").strip().upper()

            if eliminar_arreglo(eliminar, arreglos, bodega):
                print("--- ARREGLO ELIMINADO ---")
                print("")
            else:
                print("--- EL CODIGO NO EXISTE ---")
                print("")

        case 6:
            print("-- PROGRAMA FINALIZADO.. ---")
            print("")
            break