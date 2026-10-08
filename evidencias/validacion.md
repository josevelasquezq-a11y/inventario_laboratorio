Validación del sistema de inventario

1. Objetivo

Verificar que el sistema de inventario funcione correctamente y que cumpla con las funcionalidades definidas en el proyecto.

2. Pruebas realizadas

Prueba 1: Registrar un equipo

Acción:
Se seleccionó la opción "Registrar equipo" y se ingresaron los datos de un equipo.

Datos utilizados:

id_equipo: PC001

nombre: Computadora Dell

tipo_equipo: PC

estado: Disponible

ubicacion: Mesa 1

Resultado esperado:
El equipo debe registrarse correctamente y almacenarse en data/equipos.json.

Resultado obtenido:
Correcto.

Prueba 2: Validación de estado

Acción:
Se intentó registrar un equipo utilizando un estado no permitido.

Resultado esperado:
El sistema debe rechazar el estado e indicar los estados válidos.

Resultado obtenido:
Correcto. El sistema rechazó el valor ingresado y mostró los estados permitidos.

Prueba 3: Listar equipos

Acción:
Se seleccionó la opción "Listar equipos".

Resultado esperado:
El sistema debe mostrar los equipos registrados en el inventario.

Resultado obtenido:
Correcto.

Prueba 4: Buscar equipo

Acción:
Se seleccionó la opción "Buscar equipo" y se ingresó el id_equipo de un equipo registrado.

Resultado esperado:
El sistema debe mostrar la información del equipo encontrado.

Resultado obtenido:
Correcto.

Prueba 5: Modificar estado

Acción:
Se seleccionó la opción "Modificar estado" y se cambió el estado de un equipo registrado.

Resultado esperado:
El sistema debe actualizar el estado del equipo y guardar el cambio en data/equipos.json.

Resultado obtenido:
Correcto.

3. Resultado de la validación

Todas las pruebas realizadas fueron satisfactorias. Las funcionalidades principales del sistema funcionan correctamente y los datos se almacenan localmente en formato JSON.

4. Conclusión

El código generado fue ejecutado y validado mediante pruebas funcionales. El sistema cumple con las funcionalidades principales definidas para la administración de los equipos tecnológicos del laboratorio.