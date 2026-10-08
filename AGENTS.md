# Reglas para agentes de IA

## 1. Lenguaje

Python

## 2. Convenciones de nombres

Id_equipo: código del equipo
nombre: nombre del dispositivo 
tipo­_equipo: categoría del equipo
estado: estatus actual del equipo
ubicacion: en que parte del laboratorio se encuentra


## 3. Organización del código

El código debe estar organizado de forma modular y clara.

Separar las diferentes responsabilidades de la aplicación en módulos o funciones independientes cuando sea necesario.

La aplicación debe separar, como mínimo, las siguientes responsabilidades:

Gestión de equipos.

Registro y modificación de información.

Búsqueda y filtrado de equipos.

Gestión de estados.

Gestión de ubicaciones.

Validación de datos.

Almacenamiento y recuperación de información.

Interfaz gráfica.

Generación de reportes, si corresponde.

Evitar colocar toda la lógica de la aplicación en un único archivo o en una única función.

Cada función debe tener una responsabilidad específica y evitar código duplicado.

## 4. Funciones

Las funciones deben tener nombres descriptivos y realizar una única tarea principal.

Como mínimo, la aplicación debe permitir:

Registrar un nuevo equipo.

Consultar la información de un equipo.

Modificar los datos de un equipo.

Eliminar un equipo cuando corresponda.

Buscar equipos por ID, nombre, tipo, estado o ubicación.

Filtrar equipos según diferentes criterios.

Cambiar el estado de un equipo.

Consultar la cantidad de equipos registrados.

Mostrar los equipos disponibles, en uso, en mantenimiento o fuera de servicio.

Validar los datos antes de guardarlos.

Guardar y cargar la información de manera persistente.

Las funciones deben devolver resultados claros y manejar adecuadamente los errores.

## 5. Datos

Cada equipo debe contener como mínimo los siguientes datos:

Id_equipo

nombre

tipo_equipo

estado

ubicacion

El Id_equipo debe ser único y no debe existir más de un equipo con el mismo identificador.

Los campos obligatorios deben validarse antes de registrar o modificar un equipo.

Los estados permitidos deben estar definidos previamente y no deben depender de texto introducido libremente por el usuario.

Ejemplo de estados:

Disponible

En uso

En mantenimiento

Fuera de servicio

Los tipos de equipo y las ubicaciones también deben manejarse de forma consistente.

La información debe conservarse aunque la aplicación sea cerrada y posteriormente ejecutada nuevamente.

## 6. Restricciones

No modificar funcionalidades existentes sin una razón justificada.

No eliminar código funcional para solucionar un problema sin analizar previamente sus consecuencias.

No cambiar los nombres de variables, funciones, archivos o estructuras de datos existentes innecesariamente.

No crear datos ficticios o valores predeterminados que no hayan sido solicitados.

No duplicar funciones o lógica que ya exista en el proyecto.

No introducir librerías externas sin justificar previamente su necesidad.

El código debe ser compatible con Python y utilizar buenas prácticas de programación.

Los datos ingresados por el usuario deben validarse antes de ser procesados o almacenados.

La aplicación debe manejar errores de manera controlada y mostrar mensajes comprensibles al usuario.

No ocultar errores mediante excepciones vacías como except: pass.

## 7. Modificación del código

Cuando se solicite modificar el código existente:

Analizar primero el código actual.

Identificar qué parte debe modificarse.

Mantener intactas las funcionalidades que no estén relacionadas con el cambio solicitado.

Realizar la menor cantidad de modificaciones necesarias.

Evitar reescribir completamente el proyecto si no es necesario.

Mantener las convenciones de nombres y la estructura existente.

Verificar que el cambio no rompa funcionalidades previamente implementadas.

Entregar el código completo actualizado cuando sea necesario para facilitar su implementación.

Explicar brevemente qué partes fueron modificadas y por qué.

Si existe una ambigüedad en el requerimiento, no asumir una solución que pueda afectar la arquitectura del proyecto. Solicitar aclaración antes de realizar cambios importantes.

## 8. Procedimiento antes de realizar cambios

Antes de modificar cualquier código, la IA debe:

Leer y analizar el código existente.

Identificar la estructura del proyecto.

Identificar las funciones, variables y módulos relacionados con el cambio.

Determinar qué funcionalidades podrían verse afectadas.

Verificar si ya existe una función o componente que pueda reutilizarse.

Evitar crear soluciones duplicadas.

Proponer la modificación cuando esta pueda afectar significativamente la estructura del proyecto.

Realizar únicamente los cambios necesarios para cumplir el requerimiento.

Revisar el código modificado para detectar errores de sintaxis, lógica o compatibilidad.

Mantener las funcionalidades existentes que no formen parte del cambio solicitado.

La IA debe priorizar la estabilidad, claridad, mantenibilidad y consistencia del proyecto sobre la cantidad de código generado.

Cuando se solicite una nueva funcionalidad, primero debe integrarla con la arquitectura existente en lugar de crear una implementación independiente.
