"""
Módulo para la gestión de equipos del laboratorio.
"""

import json
from pathlib import Path

# Ruta predeterminada del archivo de almacenamiento según AGENTS.md
RUTA_BASE = Path(__file__).resolve().parent.parent
RUTA_EQUIPOS_POR_DEFECTO = RUTA_BASE / "data" / "equipos.json"

ESTADOS_VALIDOS = ("Disponible", "En uso", "En mantenimiento", "Fuera de servicio")


def _obtener_ruta_datos(ruta_archivo=None):
    """
    Obtiene la ruta resuelta al archivo JSON de almacenamiento de equipos.

    Args:
        ruta_archivo (str | Path | None): Ruta opcional al archivo JSON.

    Returns:
        Path: Ruta resuelta hacia el archivo JSON.
    """
    if ruta_archivo is not None:
        return Path(ruta_archivo)
    return RUTA_EQUIPOS_POR_DEFECTO


def _cargar_equipos(ruta_archivo=None):
    """
    Carga la lista de equipos desde el archivo JSON de almacenamiento.

    Maneja los casos en los que el archivo no existe, está vacío o contiene
    información en formato inválido.

    Args:
        ruta_archivo (str | Path | None): Ruta opcional al archivo JSON.

    Returns:
        list: Lista de diccionarios con los equipos registrados.

    Raises:
        ValueError: Si el contenido del archivo no es un JSON válido o no es una lista.
    """
    ruta = _obtener_ruta_datos(ruta_archivo)

    if not ruta.exists():
        return []

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
            if not contenido:
                return []
            datos = json.loads(contenido)
    except json.JSONDecodeError as error:
        raise ValueError(
            f"El archivo '{ruta}' contiene un formato JSON inválido: {error}"
        ) from error

    if not isinstance(datos, list):
        raise ValueError(
            f"El archivo '{ruta}' no contiene una lista válida de equipos."
        )

    return datos


def _guardar_equipos(equipos, ruta_archivo=None):
    """
    Guarda la lista de equipos en el archivo JSON de almacenamiento local.

    Crea el directorio contenedor automáticamente si aún no existe.

    Args:
        equipos (list): Lista de equipos a persistir.
        ruta_archivo (str | Path | None): Ruta opcional al archivo JSON.

    Raises:
        TypeError: Si el parámetro equipos no es una lista.
    """
    if not isinstance(equipos, list):
        raise TypeError("El parámetro 'equipos' debe ser una lista.")

    ruta = _obtener_ruta_datos(ruta_archivo)
    ruta.parent.mkdir(parents=True, exist_ok=True)

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(equipos, archivo, indent=4, ensure_ascii=False)


def registrar_equipo(
    id_equipo,
    nombre=None,
    tipo_equipo=None,
    estado=None,
    ubicacion=None,
    ruta_archivo=None,
    *args,
):
    """
    Registra un nuevo equipo en el inventario y persiste los datos en data/equipos.json.

    Valida que los campos obligatorios no estén vacíos, que el estado pertenezca
    a los estados válidos, que el id_equipo sea único y maneja la persistencia
    local en formato JSON conservando los datos entre ejecuciones.

    Args:
        id_equipo (str | list): Código único del equipo, o lista de equipos (para compatibilidad).
        nombre (str | None): Nombre del dispositivo.
        tipo_equipo (str | None): Categoría o tipo de equipo.
        estado (str | None): Estado actual del equipo ('Disponible', 'En uso', etc.).
        ubicacion (str | None): Ubicación dentro del laboratorio.
        ruta_archivo (str | Path | None): Ruta opcional al archivo JSON de persistencia.
        *args: Argumentos posicionales adicionales para compatibilidad de invocación.

    Returns:
        dict: Diccionario con la información del equipo registrado.

    Raises:
        ValueError: Si faltan datos obligatorios, si el estado no es válido,
                    o si el id_equipo ya existe en el inventario.
        TypeError: Si los parámetros recibidos no corresponden a los tipos esperados.
    """
    lista_externa = None

    # Compatibilidad en caso de ser invocado como registrar_equipo(equipos, id_equipo, nombre, tipo, estado, ubicacion, ruta_archivo=...)
    if isinstance(id_equipo, list):
        lista_externa = id_equipo
        id_real = nombre
        nombre_real = tipo_equipo
        tipo_real = estado
        estado_real = ubicacion
        ubicacion_real = ruta_archivo
        ruta_real = args[0] if args else None
    else:
        id_real = id_equipo
        nombre_real = nombre
        tipo_real = tipo_equipo
        estado_real = estado
        ubicacion_real = ubicacion
        ruta_real = ruta_archivo

    datos = {
        "id_equipo": str(id_real).strip() if id_real is not None else "",
        "nombre": str(nombre_real).strip() if nombre_real is not None else "",
        "tipo_equipo": str(tipo_real).strip() if tipo_real is not None else "",
        "estado": str(estado_real).strip() if estado_real is not None else "",
        "ubicacion": str(ubicacion_real).strip() if ubicacion_real is not None else "",
    }

    for campo, valor in datos.items():
        if not valor:
            raise ValueError(f"El campo '{campo}' es obligatorio y no puede estar vacío.")

    if datos["estado"] not in ESTADOS_VALIDOS:
        raise ValueError(
            f"El estado '{datos['estado']}' no es válido. "
            f"Estados permitidos: {', '.join(ESTADOS_VALIDOS)}."
        )

    # Cargar equipos almacenados desde JSON
    equipos_guardados = _cargar_equipos(ruta_real)

    # Validar unicidad en almacenamiento JSON
    for equipo in equipos_guardados:
        if equipo.get("id_equipo") == datos["id_equipo"]:
            raise ValueError(f"Ya existe un equipo con el id_equipo '{datos['id_equipo']}'.")

    # Validar unicidad en lista externa si fue provista
    if lista_externa is not None:
        for equipo in lista_externa:
            if equipo.get("id_equipo") == datos["id_equipo"]:
                raise ValueError(f"Ya existe un equipo con el id_equipo '{datos['id_equipo']}'.")

    nuevo_equipo = {
        "id_equipo": datos["id_equipo"],
        "nombre": datos["nombre"],
        "tipo_equipo": datos["tipo_equipo"],
        "estado": datos["estado"],
        "ubicacion": datos["ubicacion"],
    }

    # Agregar y guardar en JSON
    equipos_guardados.append(nuevo_equipo)
    _guardar_equipos(equipos_guardados, ruta_real)

    # Si se pasó una lista externa en memoria, actualizarla también
    if lista_externa is not None:
        lista_externa.append(nuevo_equipo)

    return nuevo_equipo
