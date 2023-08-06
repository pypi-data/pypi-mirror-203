from num2words import num2words


def numero_a_palabras(numero, idioma='es', conversor='currency'):
    """
    Convierte un número a palabras en Español usando la librería num2words https://pypi.org/project/num2words/.

    Args:
        numero (float): Número a convertir.
        idioma (str): Idioma al cual convertir el número. Por defecto es Español.
        conversor (str): Tipo de conversion a palabras quequeremos usar. Puede tener los siguientes valores:
            cardinal
            ordinal
            ordinal_num
            year
            currency (por defecto)

    Returns:
        str: El número convertido a palabras usando el idioma y conversor indicados.
    """
    return num2words(numero, lang=idioma, to=conversor)
