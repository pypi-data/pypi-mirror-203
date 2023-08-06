from jinja2 import Environment, FileSystemLoader
from arrendatools.plantillas.filters.fechas import dias_del_año, formato_fecha
from arrendatools.plantillas.filters.numeros import formato_divisa, formato_porcentaje, numero_a_palabras


def aplicar_plantilla(directorio_plantillas, plantilla, datos):
    try:
        environment = Environment(loader=FileSystemLoader(directorio_plantillas))
        template = environment.get_template(plantilla)
        return template.render(datos,
                               numero_a_palabras=numero_a_palabras,
                               formato_divisa=formato_divisa,
                               formato_porcentaje=formato_porcentaje,
                               formato_fecha=formato_fecha,
                               dias_del_año=dias_del_año)
    except Exception as e:
        return str(e)
