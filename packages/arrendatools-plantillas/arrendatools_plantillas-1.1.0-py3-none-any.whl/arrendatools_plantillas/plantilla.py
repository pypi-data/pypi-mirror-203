import locale

from jinja2 import Environment, FileSystemLoader
from arrendatools_plantillas.filters.numero_a_palabras import numero_a_palabras
from arrendatools_plantillas.filters.formato_fecha import strftime


def generar_html(directorio_plantillas, plantilla, datos):
    locale.setlocale(locale.LC_ALL, 'es_ES.utf8')
    environment = Environment(loader=FileSystemLoader(directorio_plantillas))
    environment.filters['numero_a_palabras'] = numero_a_palabras
    environment.filters['strftime'] = strftime

    template = environment.get_template(plantilla)
    return template.render(datos)
