def menu():
    print(" ========== MENÚ PRINCIPAL ==========")
    print("1. Total de reproducciones por plataforma")
    print("2. Búsqueda de series por rango de vistas")
    print("3. Actualizar precio de arriendo")
    print("4. Agregar nueva serie")
    print("5. Eliminar serie")
    print("6. Salir")
    print("=====================================")

def leer_opcion():

    while True:
        try:
            opcion = int(input("Ingrese una opcion del menu: "))
            
            if opcion > 0 and opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opcion valida.")
        except ValueError:
            print("Debe seleccionar una opcion valida.")

#-------------------------------------------- menu y opcion --------------

def total_reproducciones(plataforma, dicc_peliculas, dicc_metricas):

    cantDisp = 0

    for codigo, datos in dicc_peliculas.items():

        if plataforma == datos[1]:
            cantDisp += dicc_metricas[codigo][1]

    print("--- REPRODUCCIONES ---")
    print(f"El total de reproducciones acumuladas es: {cantDisp} mil.")
    print("")

def buscar_por_vistas(min_vistas, max_vistas, dicc_peliculas, dicc_metricas):

    lista = []

    for codigo, datos in dicc_metricas.items():

        if datos[1] >= min_vistas and datos[1] <= max_vistas:
            producto = dicc_peliculas[codigo][0]
            lista.append(f"{producto}--{codigo}")

    if len(lista) == 0:
        print("No hay series en ese rango de reproducciones.")
    else:
        lista.sort()

        print("--- LAS SERIES ENCONTRADAS SON ---")
        for datos in lista:

            print(f"{datos}")
        print("")

def buscar_codigo(codigo, dicc_peliculas):

    return codigo in dicc_peliculas

def actualizar_precio(codigo, nuevo_precio, dicc_peliculas, dicc_metricas):

    if buscar_codigo(codigo, dicc_peliculas):
        dicc_metricas[codigo][0] = nuevo_precio
        return True
    return False

#------------------------------------ funcion 1, 2, 3 ------------------------------------

def validar_codigo(codigo, dicc_peliculas):

    if codigo.strip() == "":
        return False
    if codigo in dicc_peliculas:
        return False
    return True

def validar_texto(texto): #sirve para validar (titulo, plataforma, genero)

    if texto.strip() == "":
        return False
    return True

def validar_clasificacion(clasificacion):

    return clasificacion.upper() in ["TEEN", "18+"]

def validar_original(original):

    return original.lower() in ["s", "n"]

def validar_numero(numero): #sirve para validar (precio, reproducciones)

    if numero >= 0:
        return True
    return False

#--------------------- funcion opcion 4 --------------------

def agregar_serie(dicc_peliculas, dicc_metricas):

    while True:
        codigo = input("Ingrese codigo de la serie: ").strip().upper()

        if validar_codigo(codigo, dicc_peliculas):
            break
        else:
            print("No debe quedar vacio ni existir previamente.")

    while True:
        titulo = input("Ingrese titulo: ").strip().title()

        if validar_texto(titulo):
            break
        else:
            print("No debe quedar vacio, ni tenes solo espacios en blanco.")

    while True:
        plataforma = input("Ingrese plataforma: ").strip().title()

        if validar_texto(plataforma):
            break
        else:
            print("No debe quedar vacio, ni tenes solo espacios en blanco.")

    while True:
        genero = input("Ingrese genero: ").strip().title()

        if validar_texto(genero):
            break
        else:
            print("No debe quedar vacio, ni tenes solo espacios en blanco.")

    while True:
        clasificacion = input("Ingrese clasificacion (TEEN/18+): ").strip().upper()

        if validar_clasificacion(clasificacion):
            break
        else:
            print("Debe ser exactamente (TEEN/18+).")

    while True:
        original = input("Es original? (s/n): ").strip().lower()

        if validar_original(original):
            originalbool = True if original == "s" else False
            break
        else:
            print("Debe ser exactamente (s/n).")

    while True:
        try:
            precio = input("Ingrese precio de arriendo: ").strip()
            precio = int(precio)

            if validar_numero(precio):
                break
            else:
                print("Debe ser mayor o igual a 0.")
        except ValueError:
            print("Debe ser mayor o igual a 0.")

    while True:
        try:
            reproducciones = input("Ingrese reproducciones (en miles): ").strip()
            reproducciones = int(reproducciones)

            if validar_numero(reproducciones):
                break
            else:
                print("Debe ser mayor o igual a 0.")
        except ValueError:
            print("Debe ser mayor o igual a 0.")

    dicc_peliculas[codigo] = [titulo, plataforma, genero, clasificacion, originalbool]
    dicc_metricas[codigo] = [precio, reproducciones]
    print("--- SERIE AGREGADA CON EXITO ---")
    print("")

def eliminar_serie(codigo, dicc_peliculas, dicc_metricas):

    if buscar_codigo(codigo, dicc_peliculas):
        del dicc_peliculas[codigo]
        del dicc_metricas[codigo]
        return True
    return False

peliculas = {
    'S001': ['Stranger Things', 'Netflix', 'Ciencia Ficcion', 'TEEN', True],
    'S002': ['The Mandalorian', 'Disney+', 'Sci-Fi', 'TEEN', False],
    'S003': ['The Boys', 'Prime Video', 'Accion', '18+', False]
}

metricas = {
    'S001': [0, 450],
    'S002': [2500, 120],
    'S003': [0, 890]
}

while True:

    menu()
    opcionMenu = leer_opcion()

    match opcionMenu:

        case 1:
            buscarPlataforma = input("Ingrese paltaforma a consultar: ").strip().title()
            total_reproducciones(buscarPlataforma, peliculas, metricas)

        case 2:
            while True:
                try:
                    minRepro = int(input("Ingrese el minimo de reproducciones (en miles): "))
                    maxRepro = int(input("Ingrese el maximo de reproducciones (en miles): "))

                    if minRepro >= 0 and maxRepro >= minRepro:
                        break
                    else:
                        print("Debe ingresar valores enteros.")
                except ValueError:
                    print("Debe ingresar valores enteros.")
                
            buscar_por_vistas(minRepro, maxRepro, peliculas, metricas)

        case 3:
            while True:
                codigoserie = input("Ingres codigo de la serie: ").strip().upper()

                while True:
                    try:
                        precio = int(input("Ingrese nuevo precio: "))

                        if precio >= 0:
                            break
                        else:
                            print("ERROR: debe ser un numero entero positivo.")
                    except ValueError:
                        print("ERROR: debe ser un numero entero positivo.")

                if actualizar_precio(codigoserie, precio, peliculas, metricas):
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
                        print("Debe ser (s/n).")

                if seguir == "n":
                    break

        case 4: 
            agregar_serie(peliculas, metricas)

        case 5:
            eliminar = input("Ingrese el codigo de la serie que desea eliminar: ").strip().upper()

            if eliminar_serie(eliminar, peliculas, metricas):
                print("--- SERIE ELIMINADA ---")
                print("")
            else:
                print("--- EL CODIGO NO EXISTE ---")
                print("")

        case 6:
            print("--- PROGRAMA FINALIZADO... ---")
            break
