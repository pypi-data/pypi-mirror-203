# ArrendaTools Plantillas
![License](https://img.shields.io/github/license/hokus15/ArrendaToolsPlantillas)
[![Build Status](https://github.com/hokus15/ArrendaToolsPlantillas/actions/workflows/main.yml/badge.svg)](https://github.com/hokus15/ArrendaToolsPlantillas/actions)
![GitHub last commit](https://img.shields.io/github/last-commit/hokus15/ArrendaToolsPlantillas?logo=github)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/hokus15/ArrendaToolsPlantillas?logo=github)

Módulo de Python que aplica plantillas jinja. Además inlcuye un filtro para convertir un número a letras.

## Requisitos

Este módulo requiere Python 3.7 o superior.

## Uso

A continuación se muestra un ejemplo de cómo usar el módulo:

```python
from arrendatools_plantillas.plantilla import generar_html
import json

plantilla = "prueba.html"
fichero_datos = 'prueba.json'

with open(fichero_datos, encoding='iso-8859-1') as json_file:
    data = json.load(json_file)

doc = generar_html("./", plantilla', data)

with open('prueba-rendered.html', "w") as archivo:
    archivo.write(doc)

```
