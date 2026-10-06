# Reglas para agentes de IA

## 1. Lenguaje

Python

## 2. Convenciones de nombres

•Id_equipo: codigo del equipo
•nombre: nombre del dispositivo 
•tipo¬_equipo: categoría del equipo
•estado: estatus actual del equipo
•ubicación: en que parte del laboratorio se encuentra
* *Nota general*: Todo el código (variables, funciones, clases) debe usar estrictamente **snake_case** y escribirse en **Español**.


## 3. Organización del código

Arquitectura Modular: El proyecto debe seguir el principio de separación de capas. No pongas todo el código en un solo archivo.
Estructura de archivos:
  Lógica de la interfaz gráfica en archivos de vista independientes (ej. `main_view.py`).
  Lógica de manipulación de datos y persistencia en un módulo controlador/modelo separado (ej. `database_manager.py`).

## 4. Funciones

Responsabilidad única: Cada función debe realizar una sola tarea específica.
Tamaño: Las funciones deben ser compactas y **no superar las 20 o 30 líneas de código**. Si exceden este tamaño, deben refactorizarse en submétodos.
Nombres: Deben empezar con un verbo imperativo en snake_case (ej. `registrar_equipo()`, `cargar_datos()`).
Documentación: Obligatorio incluir **Docstrings** con triple comilla (`"""`) explicando el propósito, parámetros y retorno de cada función.

## 5. Datos

Almacenamiento Local: La persistencia de datos debe ser 100% offline.
Formato: Utilizar exclusivamente archivos planos en formato **JSON** procesados con la librería nativa `json`.
Estructura: Los datos se centralizan en la carpeta raíz `data/` dentro del archivo `equipos.json`, codificado en UTF-8 y estructurado como una lista de objetos.

## 6. Restricciones

Librerías gráficas: Usar únicamente **CustomTkinter** para la interfaz visual de escritorio moderna. Queda **prohibido** el uso de Tkinter clásico u otras librerías web/móviles.
Prohibición de código incompleto: Está estrictamente **PROHIBIDO** entregar fragmentos de código con comentarios de marcador de posición como `# Agregar lógica aquí` o `# TODO`. Todo el código generado debe ser 100% funcional y ejecutable.
Variables globales: Queda prohibido el uso de variables globales para la transferencia de datos entre ventanas; se debe usar herencia o paso de parámetros por POO.
Manejo de errores: Toda operación de lectura/escritura en el archivo JSON y las interacciones de entrada en la interfaz gráfica deben estar protegidas con bloques **try-except** (ej. capturando `FileNotFoundError` o `json.JSONDecodeError`) mostrando alertas visuales controladas al usuario.

## 7. Modificación del código

Al realizar modificaciones en un módulo existente, se debe respetar la firma de las funciones actuales para no romper la compatibilidad con los demás archivos.
Cualquier refactorización debe mantener los nombres de las variables bajo el estándar `snake_case` definido en el punto 2.

## 8. Procedimiento antes de realizar cambios

Antes de reescribir o generar un nuevo bloque de código, analiza la estructura actual de carpetas y los archivos JSON existentes en `data/`.
Explica brevemente en un párrafo qué cambios vas a realizar y qué archivos se verán afectados antes de imprimir el código definitivo.

