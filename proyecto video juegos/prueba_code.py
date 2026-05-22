# Sistema de Registro de Videojuegos
import csv

archivo = "videojuegos.csv"

# Función para validar datos
def validar_datos(codigo, nombre, genero, plataforma, año):
    if codigo == "" or nombre == "" or genero == "" or plataforma == "" or año == "":
        return False
    
    if not año.isdigit():
        return False

    return True

# Función para registrar videojuegos
def registrar_videojuego():
    codigo = input("Ingrese código: ")
    nombre = input("Ingrese nombre: ")
    genero = input("Ingrese género: ")
    plataforma = input("Ingrese plataforma: ")
    año = input("Ingrese año: ")

    # Validación
    if validar_datos(codigo, nombre, genero, plataforma, año):

        # Guardar en CSV
        with open(archivo, mode="a", newline="", encoding="utf-8") as file:
            escritor = csv.writer(file)

            escritor.writerow([codigo, nombre, genero, plataforma, año])

        print("Videojuego registrado correctamente.")
    else:
        print("Error: Datos inválidos.")

# Crear archivo CSV con encabezados si no existe
try:
    with open(archivo, mode="x", newline="", encoding="utf-8") as file:
        escritor = csv.writer(file)
        escritor.writerow(["Código", "Nombre", "Género", "Plataforma", "Año"])
except FileExistsError:
    pass

# Menú principal
while True:
    print("\n=== SISTEMA DE REGISTRO DE VIDEOJUEGOS ===")
    print("1. Registrar videojuego")
    print("2. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_videojuego()

    elif opcion == "2":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")
