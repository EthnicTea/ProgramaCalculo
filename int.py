
####### Cod CHATGPT #########

import numpy as np
from scipy.optimize import minimize

def obtener_float_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("El valor debe ser mayor que cero. Inténtalo de nuevo.")
        except ValueError:
            print("Eso no es un número válido. Inténtalo de nuevo.")

def calcular_area_gabinete(alto, ancho, profundidad):
    # Calcula el área total del gabinete en metros cuadrados
    area_frontal_y_trasera = 2 * (alto * ancho)  # Frente y parte trasera
    area_laterales = 2 * (alto * profundidad)  # Lados
    area_superior_e_inferior = 2 * (ancho * profundidad)  # Parte superior e inferior
    return (area_frontal_y_trasera + area_laterales + area_superior_e_inferior) / 10000  # Convertir cm² a m²

def calcular_costo_total(area, costo_acero, costo_acrilico, proporcion_acero, proporcion_acrilico):
    # Calcula el costo total basado en las proporciones de materiales y sus costos
    costo_total_acero = area * proporcion_acero * costo_acero
    costo_total_acrilico = area * proporcion_acrilico * costo_acrilico
    return costo_total_acero + costo_total_acrilico

def objetivo_funcion(x):
    # Ejemplo de función objetivo para optimizar
    return x[0]**2 + x[1]**2  # Ejemplo simple de función cuadrática

def main():
    print("Introduce las medidas del gabinete en centímetros.")
    alto = obtener_float_positivo("Alto: ")
    ancho = obtener_float_positivo("Ancho: ")
    profundidad = obtener_float_positivo("Profundidad: ")

    print("Introduce el costo por metro cuadrado de los materiales.")
    costo_acero = obtener_float_positivo("Costo del acero: ")
    costo_acrilico = obtener_float_positivo("Costo del acrílico: ")

    print("Introduce la proporción de uso de cada material (entre 0 y 1).")
    proporcion_acero = obtener_float_positivo("Proporción de acero: ")
    proporcion_acrilico = obtener_float_positivo("Proporción de acrílico: ")

    if proporcion_acero + proporcion_acrilico != 1:
        print("Las proporciones deben sumar 1. Inténtalo de nuevo.")
        return

    area_total = calcular_area_gabinete(alto, ancho, profundidad)
    costo_total = calcular_costo_total(area_total, costo_acero, costo_acrilico, proporcion_acero, proporcion_acrilico)

    print(f"El costo total del gabinete es: {costo_total:.2f}")

    # Optimización de ejemplo usando scipy
    x0 = np.array([1, 1])  # Valores iniciales
    res = minimize(objetivo_funcion, x0)
    print(f"Optimización de ejemplo: {res}")

# Determina si el script se está ejecutando como programa principal o si está siendo importado como módulo en otro script
if __name__ == "__main__":
    main()
