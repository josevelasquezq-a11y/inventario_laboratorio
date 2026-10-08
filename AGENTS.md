# Reglas para agentes de IA

## 1. Lenguaje

El proyecto debe desarrollarse utilizando Python.

Todo el código generado debe ser compatible con Python.

Los comentarios y explicaciones del código deben estar redactados en español.

## 2. Convenciones de nombres

Utilizar exclusivamente la convención snake_case para variables, funciones, métodos y nombres de archivos Python.

Los nombres de los datos de los equipos deben respetar las siguientes convenciones:

-id_equipo: código único del equipo.

-nombre: nombre del dispositivo.

-tipo_equipo: categoría del equipo.

-estado: estado actual del equipo.

-ubicacion: lugar donde se encuentra el equipo dentro del laboratorio.

Ejemplos correctos:

id_equipo
tipo_equipo
obtener_equipo()
registrar_equipo()

No utilizar nombres como:

idEquipo
tipoEquipo
ObtenerEquipo()

## 3. Organización del código

Respetar la estructura existente del proyecto.

La aplicación debe mantener separadas las responsabilidades de cada módulo.

La estructura esperada es:

inventario-laboratorio/
├── README.md
├── AGENTS.md
├── app.py
├── src/
│   ├── inventario.py
│   └── mantenimiento.py
├── data/
│   └── equipos.json
└── evidencias/
    └── validacion.md

app.py debe encargarse del inicio y coordinación de la aplicación.

src/inventario.py debe contener la lógica relacionada con la gestión de los equipos.

src/mantenimiento.py debe contener la lógica relacionada con el mantenimiento de los equipos.

data/equipos.json debe utilizarse para el almacenamiento local de los equipos.

No mezclar innecesariamente responsabilidades entre los módulos.

## 4. Funciones

Las funciones deben tener una responsabilidad clara y utilizar nombres descriptivos en snake_case.

La aplicación debe permitir, según las funcionalidades definidas en el proyecto:

-Registrar equipos.

-Listar equipos.

-Buscar equipos.

-Modificar el estado de un equipo.

-Gestionar la información de los equipos.

-Gestionar el mantenimiento de los equipos.

Evitar duplicar funciones o implementar nuevamente una funcionalidad que ya exista.

## 5. Datos

El almacenamiento de los equipos debe realizarse localmente mediante un archivo JSON.

El archivo definido para el almacenamiento es:

data/equipos.json

Cada equipo debe contener como mínimo:

id_equipo
nombre
tipo_equipo
estado
ubicacion

No cambiar JSON por otro sistema de almacenamiento sin autorización explícita.

No crear sistemas de almacenamiento alternativos.

La información debe conservarse correctamente entre ejecuciones del programa.

El código debe manejar adecuadamente los casos en los que el archivo JSON no exista, esté vacío o contenga información inválida.

## 6. Restricciones

La IA debe cumplir las siguientes restricciones:

Utilizar Python.

Utilizar snake_case.

Mantener el almacenamiento local en data/equipos.json.

No utilizar librerías no autorizadas.

No utilizar librerías desactualizadas.

No proponer arquitecturas web.

No crear conexiones externas.

No modificar innecesariamente la estructura del proyecto.

No crear funcionalidades que no hayan sido solicitadas.

No utilizar marcadores de posición en el código final.

No dejar funciones incompletas.

No omitir el manejo de errores.

## 7. Modificación del código

Cuando se solicite modificar el código:

- Analizar primero el código existente.

- Identificar los archivos relacionados con el cambio.

- Reutilizar las funciones existentes cuando sea posible.

- Modificar únicamente lo necesario.

- Mantener las funcionalidades existentes que no estén relacionadas con el cambio.

- Respetar la estructura actual del proyecto.

- Respetar las convenciones de nombres.

- Respetar el almacenamiento en data/equipos.json.

- No incorporar librerías no autorizadas.

- Verificar que el código modificado sea compatible con Python.

- Verificar que no se hayan introducido errores.

- Entregar código completo y funcional para la parte modificada.

## 8. Procedimiento antes de realizar cambios

Antes de generar o modificar código, la IA debe:

- Leer y analizar AGENTS.md.

- Revisar la estructura actual del proyecto.

- Revisar los archivos relacionados con la tarea.

- Identificar las funciones y componentes existentes que puedan reutilizarse.

- Determinar qué archivos necesitan ser modificados.

- Evitar modificaciones innecesarias.

- Mantener el almacenamiento local definido.

- Mantener las dependencias autorizadas.

- Generar únicamente los cambios necesarios.

- Validar el código generado antes de considerarlo terminado.

## Documentación

- Todas las funciones deben incluir docstring.
- El docstring debe describir brevemente el propósito de la función.

