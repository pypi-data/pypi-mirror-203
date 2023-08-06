import calendar
from dateutil import parser
from babel.dates import format_datetime, get_timezone


def dias_del_año(año):
    """
    Calcula los dias que tiene un año teniendo en cuenta si es bisiesto o no

    Args:
        año (int): Año para calcular los dias.

    Returns:
        int: Numero de dias del año indicado
    """

    if calendar.isleap(año):
        return 366
    else:
        return 365


def formato_fecha(fecha_hora=None, formato='medium', tzinfo='Europe/Madrid', locale='es_ES'):
    """
    Convierte una fecha dada en formato ISO8601 al formato especificado. Ver https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

    Args:

        fecha_hora (): fecha en formato ISO8601. Si no se pasa ninguna se usa la fecha y hora actual
        formato (): uno de  “full”, “long”, “medium”, o “short”, o un patron datetime personalizado. "medium" por defecto.
        tzinfo (): la zona horaria a aplicar para dar formato a la fecha-hora. "Europe/Madrid" por defecto.
        locale (): identificador de locale. es_ES por defecto.

    Returns:
        str: La fecha en texto con el formato indicado
    """
    date = None
    time_zone = get_timezone(tzinfo)
    if isinstance(fecha_hora, str):
        date = parser.parse(fecha_hora)

    return format_datetime(date, formato, time_zone, locale)
