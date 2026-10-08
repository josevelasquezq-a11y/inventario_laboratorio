# Reglas para agentes de IA

## 1. Lenguaje

El proyecto debe desarrollarse utilizando Python.

Todo el código, nombres de variables, funciones, comentarios y documentación interna deben respetar el idioma acordado para el proyecto.

## 2. Convenciones de nombres

Utilizar exclusivamente la convención snake_case para:

Variables.

Funciones.

Métodos.

Archivos Python.

Identificadores relacionados con los datos.

Ejemplos:

id_equipo
nombre_equipo
tipo_equipo
obtener_equipo()
registrar_equipo()

Evitar convenciones como:

idEquipo
nombreEquipo
NombreEquipo

Los nombres deben ser descriptivos y mantener consistencia en todo el proyecto.

Los campos principales de un equipo son:

id_equipo: identificador único del equipo.

nombre: nombre del dispositivo.

tipo_equipo: categoría del dispositivo.

estado: estado actual del equipo.

ubicacion: ubicación del equipo dentro del laboratorio.


## 3. Organización del código

Respetar la estructura existente del proyecto.

No reorganizar archivos, carpetas, módulos o componentes que ya funcionen correctamente, salvo que el cambio sea estrictamente necesario.

Cada componente debe mantener una responsabilidad clara.

Evitar:

Duplicar código.

Crear funciones innecesarias.

Colocar toda la lógica en un único archivo.

Crear archivos o carpetas sin una justificación funcional.

Modificar componentes que no estén relacionados con el requerimiento solicitado.

Antes de crear una nueva función, clase o módulo, comprobar si ya existe uno que pueda reutilizarse.

## 4. Funciones

Las funciones deben tener una responsabilidad específica y utilizar nombres descriptivos en snake_case.

La aplicación debe permitir, según las funcionalidades implementadas:

Registrar equipos.

Consultar equipos.

Modificar equipos.

Eliminar equipos.

Buscar equipos.

Filtrar equipos.

Cambiar el estado de un equipo.

Gestionar las ubicaciones.

Validar los datos ingresados.

Guardar y recuperar la información.

No crear funciones duplicadas cuando ya exista una función que cumpla la misma finalidad.

## 5. Datos

Las funciones deben tener una responsabilidad específica y utilizar nombres descriptivos en snake_case.

La aplicación debe permitir, según las funcionalidades implementadas:

Registrar equipos.

Consultar equipos.

Modificar equipos.

Eliminar equipos.

Buscar equipos.

Filtrar equipos.

Cambiar el estado de un equipo.

Gestionar las ubicaciones.

Validar los datos ingresados.

Guardar y recuperar la información.

No crear funciones duplicadas cuando ya exista una función que cumpla la misma finalidad.

## 6. Restricciones

No utilizar librerías externas que no hayan sido autorizadas para el proyecto.

Antes de incorporar una nueva librería:

Comprobar si la funcionalidad puede implementarse utilizando las librerías ya disponibles.

Si no es posible, solicitar autorización para incorporar una nueva dependencia.

No instalar ni importar automáticamente librerías no autorizadas.

No reemplazar una librería existente por otra sin autorización.

## 7. Modificación del código

Cuando se solicite modificar el proyecto:

Analizar primero el código existente.

Identificar exactamente qué parte debe modificarse.

Reutilizar las funciones y componentes existentes cuando sea posible.

Modificar únicamente lo necesario para cumplir el requerimiento.

Mantener intactas las funcionalidades que no estén relacionadas con el cambio.

Mantener la estructura actual del proyecto.

Mantener las convenciones de nombres existentes.

No incorporar librerías no autorizadas.

No cambiar el sistema de almacenamiento.

Comprobar que el cambio no introduzca errores en funcionalidades existentes.

La prioridad es realizar el cambio mínimo necesario, manteniendo la estabilidad y coherencia del proyecto.

## 8. Procedimiento antes de realizar cambios

Antes de modificar cualquier archivo, la IA debe:

Analizar la estructura actual del proyecto.

Revisar los archivos relacionados con el requerimiento.

Identificar las funciones y componentes existentes que puedan reutilizarse.

Comprobar las dependencias utilizadas.

Verificar el sistema de almacenamiento existente.

Determinar qué archivos necesitan realmente ser modificados.

Evitar modificaciones innecesarias.

Realizar únicamente los cambios solicitados.

Verificar que el código siga respetando las reglas de este archivo.

Revisar que las funcionalidades existentes continúen funcionando.

Si el requerimiento no está suficientemente claro y realizar el cambio podría afectar la estructura, las dependencias o el almacenamiento del proyecto, solicitar aclaración antes de realizar modificaciones importantes.

## Documentación

- Todas las funciones deben incluir docstring.
- El docstring debe describir brevemente el propósito de la función.
