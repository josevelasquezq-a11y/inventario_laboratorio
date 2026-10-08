# Sistema de Inventario de Laboratorio

## 1. Descripción

Se quiere desarrollar una aplicación para administrar el equipo tecnológico de un laboratorio

## 2. Objetivo

Poder administrar los equipo que se encuentran en el laboratorio, hacer inventario.

## 3. Usuarios

Administradores del laboratorio

## 4. Funcionalidades

-Registrar equipo
-Listar equipos
-Buscar equipo
-Modificar estado

## 5. Información de los equipos

Cada equipo contiene:

- `id_equipo`: código único del equipo.
- `nombre`: nombre del dispositivo.
- `tipo_equipo`: categoría del equipo.
- `estado`: estado actual del equipo.
- `ubicacion`: lugar donde se encuentra dentro del laboratorio.

## 6. Tecnologías

Lenguaje:Python

Almacenamiento: La información de los equipos se almacenará localmente en formato JSON.

El archivo de almacenamiento será:

`data/equipos.json`

## 7. Estructura del proyecto

El proyecto deberá mantener la siguiente estructura:

inventario_laboratorio/
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

## 8. Ejecución

Se ejecutara el programa con el código generado por la IA para verificar su funcionamiento.
