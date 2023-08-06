from jinja2 import Environment, FileSystemLoader
from arrendatools_plantillas.filters.numero_a_palabras import numero_a_palabras
from arrendatools_plantillas.filters.formato_fecha import strftime


def aplicar_plantilla(directorio_plantillas, plantilla, datos):
    environment = Environment(loader=FileSystemLoader(directorio_plantillas))
    environment.filters['numero_a_palabras'] = numero_a_palabras
    environment.filters['strftime'] = strftime

    template = environment.get_template(plantilla)
    return template.render(datos)
