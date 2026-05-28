import csv

archivo = "videojuegos.csv"


def validar_datos(codigo, nombre, genero, plataforma, año):

    if codigo == "" or nombre == "" or genero == "" or plataforma == "" or año == "":
        return False

    if not año.isdigit():
        return False

    return True



def registrar_videojuego():

    codigo = input("Ingrese código: ")
    nombre = input("Ingrese nombre: ")
    genero = input("Ingrese género: ")
    plataforma = input("Ingrese plataforma: ")
    año = input("Ingrese año: ")


    if validar_datos(codigo, nombre, genero, plataforma, año):

        
        with open(archivo, mode="a", newline="", encoding="utf-8") as file:

            escritor = csv.writer(file)

            escritor.writerow([
                codigo,
                nombre,
                genero,
                plataforma,
                año
            ])

        print("Videojuego registrado correctamente.")

    else:
        print("Error: Datos inválidos.")



def editar_videojuego():

    codigo_buscar = input("Ingrese el código del videojuego a editar: ")

    videojuegos = []
    encontrado = False

    try:

        
        with open(archivo, mode="r", newline="", encoding="utf-8") as file:

            lector = csv.reader(file)

            for fila in lector:

                # Evitar filas vacías
                if len(fila) == 0:
                    continue

                # Mantener encabezado
                if fila[0] == "Código":
                    videojuegos.append(fila)
                    continue

                # Buscar videojuego
                if fila[0] == codigo_buscar:

                    encontrado = True

                    print("\n=== Videojuego Encontrado ===")
                    print("Código:", fila[0])
                    print("Nombre:", fila[1])
                    print("Género:", fila[2])
                    print("Plataforma:", fila[3])
                    print("Año:", fila[4])

                    print("\n=== Editando videojuego ===")

                    # Nuevos datos
                    nuevo_nombre = input("Ingrese nuevo nombre (dejar en blanco para mantener): ")
                    nuevo_genero = input("Ingrese nuevo género (dejar en blanco para mantener): ")
                    nueva_plataforma = input("Ingrese nueva plataforma (dejar en blanco para mantener): ")
                    nuevo_año = input("Ingrese nuevo año (dejar en blanco para mantener): ")

                    # Mantener datos antiguos
                    if nuevo_nombre == "":
                        nuevo_nombre = fila[1]

                    if nuevo_genero == "":
                        nuevo_genero = fila[2]

                    if nueva_plataforma == "":
                        nueva_plataforma = fila[3]

                    if nuevo_año == "":
                        nuevo_año = fila[4]

                    # Validar datos
                    if validar_datos(
                        codigo_buscar,
                        nuevo_nombre,
                        nuevo_genero,
                        nueva_plataforma,
                        nuevo_año
                    ):

                        videojuegos.append([
                            codigo_buscar,
                            nuevo_nombre,
                            nuevo_genero,
                            nueva_plataforma,
                            nuevo_año
                        ])

                        print("Videojuego actualizado correctamente.")

                    else:
                        print("Error: Datos inválidos.")
                        videojuegos.append(fila)

                else:
                    videojuegos.append(fila)

       
        if encontrado:

            with open(archivo, mode="w", newline="", encoding="utf-8") as file:

                escritor = csv.writer(file)
                escritor.writerows(videojuegos)

        else:
            print("Error: El código buscado no existe en el registro.")

    except FileNotFoundError:
        print("Error: El archivo no existe.")



try:

    with open(archivo, mode="x", newline="", encoding="utf-8") as file:

        escritor = csv.writer(file)

        escritor.writerow([
            "Código",
            "Nombre",
            "Género",
            "Plataforma",
            "Año"
        ])

except FileExistsError:
    pass



while True:

    print("\n=== SISTEMA DE REGISTRO DE VIDEOJUEGOS ===")
    print("1. Registrar videojuego")
    print("2. Actualizar videojuego")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_videojuego()

    elif opcion == "2":
        editar_videojuego()

    elif opcion == "3":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")
