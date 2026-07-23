# Generador de horarios universitarios con Python

Programa desarrollado en Python para generar combinaciones de horarios universitarios, eliminar aquellas que presentan traslapes y mostrar las mejores opciones de acuerdo con preferencias personales de profesores.

El proyecto surgió como una herramienta para facilitar la selección de materias durante el proceso de reinscripción.

## Ejemplo de resultado

![Ejemplo de horario generado](assets/horario-demostracion.jpg)

## Funcionalidades

- Almacena la información de cada materia, grupo, profesor y horario.
- Genera todas las combinaciones posibles de grupos.
- Detecta materias que se imparten en el mismo día y bloque horario.
- Elimina automáticamente los horarios con traslapes.
- Asigna un puntaje a cada combinación según preferencias personales.
- Ordena los horarios válidos de mayor a menor puntaje.
- Muestra las diez mejores opciones en forma de tabla semanal.
- Incluye el detalle de los profesores correspondientes a cada horario.

## ¿Cómo funciona?

Cada grupo se representa mediante un objeto de la clase `Materia`, que contiene:

- Nombre de la materia.
- Grupo.
- Profesor.
- Días y bloques en los que se imparte.

El programa utiliza `itertools.product()` para obtener todas las combinaciones posibles, seleccionando un grupo por cada materia.

Después, compara las materias de cada combinación para determinar si dos clases coinciden en el mismo día y horario.

Las combinaciones válidas reciben un puntaje basado en un diccionario de preferencias. Finalmente, los resultados se ordenan y se muestran en la terminal.

## Conceptos utilizados

- Programación orientada a objetos.
- Clases y objetos.
- Funciones.
- Listas y diccionarios.
- Ciclos y condicionales.
- Producto cartesiano con `itertools.product`.
- Validación de combinaciones.
- Funciones como criterio de ordenamiento.
- Formateo de tablas en la terminal.

## Estructura del proyecto

```text
generador-horarios-python/
│
├── generador_horarios.py
├── README.md
└── assets/
    └── horario-demostracion.jpg
```

## Requisitos

- Python 3

El programa utiliza únicamente módulos incluidos en la biblioteca estándar de Python, por lo que no es necesario instalar dependencias adicionales.

## Ejecución

Descarga o clona el repositorio y ejecuta:

```bash
python generador_horarios.py
```

El programa mostrará:

1. La cantidad total de horarios válidos encontrados.
2. Las diez combinaciones con mayor puntuación.
3. Una tabla semanal para cada opción.
4. El detalle de los grupos y profesores seleccionados.

## Sistema de puntuación

Cada profesor recibe un valor numérico de acuerdo con una preferencia personal.

El puntaje total de un horario se obtiene sumando los valores correspondientes a los profesores que aparecen en esa combinación.

Este sistema no representa una evaluación general de los docentes, sino únicamente preferencias utilizadas para ordenar los resultados del programa.

## Limitaciones

- La información de materias y grupos está escrita directamente en el código.
- Los datos corresponden a un periodo escolar específico.
- Los horarios solamente se comparan mediante bloques previamente definidos.
- Las preferencias son personales y deben modificarse para cada usuario.
- El programa actualmente muestra los resultados únicamente en la terminal.

## Posibles mejoras

- Leer las materias desde un archivo CSV o JSON.
- Permitir que el usuario indique sus preferencias.
- Agregar filtros para evitar clases demasiado temprano o demasiado tarde.
- Permitir seleccionar días libres.
- Considerar tiempos muertos entre clases.
- Exportar los horarios a CSV, HTML o PDF.
- Crear una interfaz gráfica o una aplicación web.
- Separar los datos, la lógica y la presentación en distintos archivos.

## Aprendizajes

Con este proyecto practiqué cómo representar un problema real mediante clases y estructuras de datos, generar combinaciones, detectar conflictos entre horarios y ordenar resultados según diferentes criterios.

También aprendí a presentar información de manera organizada directamente desde la terminal.

## Nota

Este proyecto fue creado con fines educativos y personales. Los datos utilizados pueden quedar desactualizados y deben modificarse para cada periodo escolar.
