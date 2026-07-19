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

    if not lista_numeros:
        logging.warning(
            "INC-002 - No se puede calcular el promedio de una lista vacía"
        )
        return None

    total = 0

    for n in lista_numeros:
        total += n

    resultado = total / len(lista_numeros)

    logging.info(
        "Promedio calculado correctamente. cantidad=%s, resultado=%s",
        len(lista_numeros),
        resultado
    )

    return resultado


def obtener_elemento(lista, indice):
    """Devuelve un elemento de la lista según el índice indicado."""

    if indice < 0 or indice >= len(lista):
        logging.warning(
            "INC-003 - Índice fuera de rango. indice=%s, longitud=%s",
            indice,
            len(lista)
        )
        return None

    elemento = lista[indice]

    logging.info(
        "Elemento obtenido correctamente. indice=%s, valor=%s",
        indice,
        elemento
    )

    return elemento

def calcular_total(precios):
    """Suma los precios de una lista."""

    total = 0

    for p in precios:
        if not isinstance(p, (int, float)):
            logging.error(
                "INC-004 - Valor no numérico detectado en precios. valor=%s",
                p
            )
            return None

        total += p

    logging.info(
        "Total de precios calculado correctamente. total=%s",
        total
    )

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
        resultado_promedio = promedio(datos)

        if resultado_promedio is None:
            print("No se puede calcular el promedio de una lista vacía.")
        else:
            print("Promedio:", resultado_promedio)

    except Exception as error:
        logging.error(
            "INC-002 - Error inesperado al calcular el promedio: %s",
            str(error)
        )

        logging.error(
            "Detalle de la excepción:\n%s",
            traceback.format_exc()
        )

    try:
        lista = [1, 2, 3]
        resultado_elemento = obtener_elemento(lista, 5)

        if resultado_elemento is None:
            print("El índice solicitado está fuera del rango de la lista.")
        else:
            print("Elemento:", resultado_elemento)

    except Exception as error:
        logging.error(
            "INC-003 - Error inesperado al obtener el elemento: %s",
            str(error)
        )

        logging.error(
            "Detalle de la excepción:\n%s",
            traceback.format_exc()
        )

    try:
        precios = [10, 20, "treinta", 40]
        resultado_total = calcular_total(precios)

        if resultado_total is None:
            print(
                "No se pudo calcular el total porque existe "
                "un valor no numérico en la lista de precios."
            )
        else:
            print("Total de precios:", resultado_total)

    except Exception as error:
        logging.error(
            "INC-004 - Error inesperado al calcular el total: %s",
            str(error)
        )

        logging.error(
            "Detalle de la excepción:\n%s",
            traceback.format_exc()
        )

    logging.info("Fin del programa")


if __name__ == "__main__":
    main()