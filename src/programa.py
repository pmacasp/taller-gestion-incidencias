"""
Este programa contiene errores simples de lógica y ejecución.
El objetivo es detectar, registrar, corregir y documentar cada incidencia.
"""

import logging
import traceback


logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8",
    filemode="w"

)


def dividir(a, b):
    """Devuelve la división de dos números."""

    if b == 0:
        logging.warning(
            "INC-001 - Intento de división entre cero. a=%s, b=%s",
            a,
            b
        )
        return None

    resultado = a / b

    logging.info(
        "División realizada correctamente. a=%s, b=%s, resultado=%s",
        a,
        b,
        resultado
    )

    return resultado


def promedio(lista_numeros):
    """Calcula el promedio de una lista de números."""
    total = 0

    for n in lista_numeros:
        total += n

    return total / len(lista_numeros)


def obtener_elemento(lista, indice):
    """Devuelve un elemento de la lista según el índice indicado."""
    return lista[indice]


def calcular_total(precios):
    """Suma los precios de una lista."""
    total = 0

    for p in precios:
        total += p

    return total


def main():
    logging.info("Inicio del programa")

    try:
        resultado_div = dividir(10, 0)

        if resultado_div is None:
            print("No se puede realizar una división entre cero.")
        else:
            print("Resultado de la división:", resultado_div)

    except Exception as error:
        logging.error(
            "INC-001 - Error inesperado en la división: %s",
            str(error)
        )

        logging.error(
            "Detalle de la excepción:\n%s",
            traceback.format_exc()
        )

    try:
        datos = []
        print("Promedio:", promedio(datos))

    except Exception as error:
        logging.error(
            "INC-002 - Error al calcular el promedio: %s",
            str(error)
        )

        logging.error(
            "Detalle de la excepción:\n%s",
            traceback.format_exc()
        )

    try:
        lista = [1, 2, 3]
        print("Elemento:", obtener_elemento(lista, 5))

    except Exception as error:
        logging.error(
            "INC-003 - Error al obtener el elemento de la lista: %s",
            str(error)
        )

        logging.error(
            "Detalle de la excepción:\n%s",
            traceback.format_exc()
        )

    try:
        precios = [10, 20, "treinta", 40]
        print("Total de precios:", calcular_total(precios))

    except Exception as error:
        logging.critical(
            "INC-004 - Error al calcular el total de precios: %s",
            str(error)
        )

        logging.critical(
            "Detalle de la excepción:\n%s",
            traceback.format_exc()
        )

    logging.info("Fin del programa")


if __name__ == "__main__":
    main()