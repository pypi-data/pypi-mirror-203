from dateutil import parser


def strftime(fecha, formato='%d de %B de %Y'):
    """
    Convierte una fecha en string con formato ISO8601 al formato especificado. Ver https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

    Args:
        fecha (str): Fecha en formato ISO8601.
        formato (str): Formato a convertir la fecha. Ver: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior. El formato por defecto es: '%-d de %B de %Y'.

    Returns:
        str: La fecha formateada con el formato indicado
    """

    date = parser.parse(fecha)
    return date.strftime(formato)
