from jinja2 import Environment, FileSystemLoader
from arrendatools_plantillas.filters.numero_a_palabras import numero_a_palabras


def generar_html(directorio_plantillas, plantilla, datos):
    environment = Environment(loader=FileSystemLoader(directorio_plantillas))
    environment.filters['numero_a_palabras'] = numero_a_palabras
    template = environment.get_template(plantilla)
    return template.render(datos)
