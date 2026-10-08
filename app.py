"""
Punto de entrada y coordinación de la aplicación de inventario de laboratorio.
"""

import sys
from pathlib import Path

# Garantizar que el directorio raíz del proyecto forme parte de sys.path
DIRECTORIO_RAIZ = Path(__file__).resolve().parent
if str(DIRECTORIO_RAIZ) not in sys.path:
    sys.path.insert(0, str(DIRECTORIO_RAIZ))

from src.inventario import (
    ESTADOS_VALIDOS,
    _cargar_equipos,
    _guardar_equipos,
    registrar_equipo,
)


def mostrar_menu():
    """
    Muestra el menú principal de opciones de la aplicación en la consola.
    """
    print("\n" + "=" * 50)
    print("      SISTEMA DE INVENTARIO DE LABORATORIO      ")
    print("=" * 50)
    print("1. Registrar equipo")
    print("2. Listar equipos")
    print("3. Buscar equipo por id_equipo")
    print("4. Modificar estado de un equipo")
    print("5. Salir")
    print("=" * 50)


def ejecutar_registrar_equipo():
    """
    Gestiona la interacción con el usuario para registrar un nuevo equipo.
    """
    print("\n--- REGISTRAR EQUIPO ---")
    id_equipo = input("Ingrese el id_equipo: ").strip()
    nombre = input("Ingrese el nombre del equipo: ").strip()
    tipo_equipo = input("Ingrese el tipo de equipo: ").strip()

    print(f"Estados válidos: {', '.join(ESTADOS_VALIDOS)}")
    estado = input("Ingrese el estado: ").strip()
    ubicacion = input("Ingrese la ubicación dentro del laboratorio: ").strip()

    try:
        equipo_registrado = registrar_equipo(
            id_equipo=id_equipo,
            nombre=nombre,
            tipo_equipo=tipo_equipo,
            estado=estado,
            ubicacion=ubicacion,
        )
        print("\n¡Equipo registrado exitosamente!")
        print(f"ID: {equipo_registrado['id_equipo']}")
        print(f"Nombre: {equipo_registrado['nombre']}")
        print(f"Tipo: {equipo_registrado['tipo_equipo']}")
        print(f"Estado: {equipo_registrado['estado']}")
        print(f"Ubicación: {equipo_registrado['ubicacion']}")
    except ValueError as error_validacion:
        print(f"\nError al registrar el equipo: {error_validacion}")
    except Exception as error_inesperado:
        print(f"\nOcurrió un error inesperado al registrar el equipo: {error_inesperado}")


def ejecutar_listar_equipos():
    """
    Gestiona la visualización de todos los equipos registrados en el inventario.
    """
    print("\n--- LISTA DE EQUIPOS EN EL LABORATORIO ---")
    try:
        equipos = _cargar_equipos()
    except ValueError as error_archivo:
        print(f"Error al cargar los datos del inventario: {error_archivo}")
        return

    if not equipos:
        print("No hay equipos registrados actualmente en el inventario.")
        return

    print(f"{'ID':<12} | {'NOMBRE':<25} | {'TIPO':<18} | {'ESTADO':<18} | {'UBICACIÓN':<20}")
    print("-" * 100)
    for equipo in equipos:
        id_eq = equipo.get("id_equipo", "N/A")
        nom = equipo.get("nombre", "N/A")
        tipo = equipo.get("tipo_equipo", "N/A")
        est = equipo.get("estado", "N/A")
        ubi = equipo.get("ubicacion", "N/A")
        print(f"{id_eq:<12} | {nom:<25} | {tipo:<18} | {est:<18} | {ubi:<20}")
    print(f"\nTotal de equipos registrados: {len(equipos)}")


def ejecutar_buscar_equipo():
    """
    Gestiona la búsqueda y visualización de un equipo por su id_equipo.
    """
    print("\n--- BUSCAR EQUIPO POR ID ---")
    id_equipo = input("Ingrese el id_equipo a buscar: ").strip()
    if not id_equipo:
        print("El id_equipo no puede estar vacío.")
        return

    try:
        equipos = _cargar_equipos()
    except ValueError as error_archivo:
        print(f"Error al consultar el inventario: {error_archivo}")
        return

    equipo_encontrado = None
    for equipo in equipos:
        if equipo.get("id_equipo") == id_equipo:
            equipo_encontrado = equipo
            break

    if equipo_encontrado:
        print("\n¡Equipo encontrado!")
        print(f"  - ID: {equipo_encontrado.get('id_equipo')}")
        print(f"  - Nombre: {equipo_encontrado.get('nombre')}")
        print(f"  - Tipo: {equipo_encontrado.get('tipo_equipo')}")
        print(f"  - Estado: {equipo_encontrado.get('estado')}")
        print(f"  - Ubicación: {equipo_encontrado.get('ubicacion')}")
    else:
        print(f"No se encontró ningún equipo con el id_equipo '{id_equipo}'.")


def ejecutar_modificar_estado():
    """
    Gestiona la modificación del estado actual de un equipo registrado.
    """
    print("\n--- MODIFICAR ESTADO DE UN EQUIPO ---")
    id_equipo = input("Ingrese el id_equipo del equipo a modificar: ").strip()
    if not id_equipo:
        print("El id_equipo no puede estar vacío.")
        return

    try:
        equipos = _cargar_equipos()
    except ValueError as error_archivo:
        print(f"Error al consultar el inventario: {error_archivo}")
        return

    indice_encontrado = -1
    for indice, equipo in enumerate(equipos):
        if equipo.get("id_equipo") == id_equipo:
            indice_encontrado = indice
            break

    if indice_encontrado == -1:
        print(f"No se encontró ningún equipo con el id_equipo '{id_equipo}'.")
        return

    equipo_actual = equipos[indice_encontrado]
    print(f"Equipo seleccionado: {equipo_actual.get('nombre')} (Estado actual: {equipo_actual.get('estado')})")
    print(f"Estados válidos permitidos: {', '.join(ESTADOS_VALIDOS)}")

    nuevo_estado = input("Ingrese el nuevo estado: ").strip()
    if nuevo_estado not in ESTADOS_VALIDOS:
        print(
            f"Estado inválido. Debe elegir uno de los estados permitidos: {', '.join(ESTADOS_VALIDOS)}."
        )
        return

    equipo_actual["estado"] = nuevo_estado
    try:
        _guardar_equipos(equipos)
        print(f"\n¡Estado actualizado exitosamente a '{nuevo_estado}' para el equipo '{id_equipo}'!")
    except Exception as error_guardado:
        print(f"Error al guardar los cambios en el almacenamiento: {error_guardado}")


def iniciar_aplicacion():
    """
    Inicia el bucle interactivo principal de la aplicación.
    """
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == "1":
            ejecutar_registrar_equipo()
        elif opcion == "2":
            ejecutar_listar_equipos()
        elif opcion == "3":
            ejecutar_buscar_equipo()
        elif opcion == "4":
            ejecutar_modificar_estado()
        elif opcion == "5":
            print("\nGracias por utilizar el Sistema de Inventario de Laboratorio. ¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Por favor, ingrese un número del 1 al 5.")


if __name__ == "__main__":
    iniciar_aplicacion()

