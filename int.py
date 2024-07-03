
####### Cod CHATGPT #########
from os import system 
import math
import sympy as sp 
#import numpy as np
#from scipy.optimize import minimize
system("cls");
print("");
print(".... Bienvenido....");
print("");
print("=================================")
print(".... Menu ....");
print("=================================");
print("  1.-  Calcular la Utilidad  ");
print("  2.-  Calcular Utilidad Maxima  ");
print("  3.-  Salir del Programa   ");
print("=================================");
print("");
Opc = None  # Inicializamos Opc con None para asegurar que entre al bucle la primera vez
while Opc not in [1, 2]:  # Mientras Opc no sea 1 o 2, repetir la solicitud
    try:
        Opc = int(input("Ingrese opción (1-2): ").strip())  # Pedimos la opción y la convertimos a entero
        if Opc not in [1, 2]:  # Si la opción no está en el rango deseado, mostrar mensaje de error
            print("Por favor ingrese una opción válida (1-2)")
    except ValueError:  # Si no se puede convertir a entero, mostrar mensaje de error
        print("Por favor ingrese una opción válida (1-2)")
print("")
if(Opc == 1):
    print("===============================================");
    print(".... Haz seleccionado Calcular la Utilidad ....");
    print("===============================================");
    print("");
    print("===================================");
    while True:
        try:
            Valor1 = input("Ingrese un valor: ").strip()  # Pedimos el valor y eliminamos espacios en blanco alrededor
            if Valor1 == "":  # Si el usuario deja el campo en blanco
                raise ValueError("No ha ingresado ningún valor")
            
            x = float(Valor1)  # Intentamos convertir el valor a un número flotante
            
            # Si llegamos hasta aquí, hemos obtenido con éxito un número
            break  # Salimos del bucle while porque tenemos el valor correcto
        except ValueError as e:
            print(f"Error: {e}. Por favor ingrese un número válido.")
    Venta = (5500*x);
    Costo = (214.812*x**2+1395.14*math.sqrt(x));
    Utilidad = Venta-Costo;
    print("===================================");
    print("");
    print("======================================");
    print(".......... MUESTRA DE DATOS ..........")
    print("======================================");
    print(".... La venta es    : ",Venta,"....");
    print(".... El costo es    : ",Costo,"....");
    print(".... La utilidad es : ",Utilidad,"....");
    print("======================================");
if(Opc == 2):
    print("===============================================");
    print(".... Haz seleccionado Calcular la Utilidad Maxima ....");
    print("===============================================");
    print("");
    print("===================================");
    x = sp.Symbol('x')
    Venta = (5500*x);
    Costo = (214.812*x**2+1395.14*sp.sqrt(x));
    Utilidad = (Venta-Costo);
    derivada = sp.diff(Utilidad, x);
    derivada_segunda = sp.diff(derivada, x)

    # Encontrar los puntos críticos (donde la primera derivada es cero o indefinida)
    puntos_criticos = sp.solve(derivada, x)

    # Evaluar la segunda derivada en los puntos críticos para determinar los extremos
    extremos = []
    for punto in puntos_criticos:
        segunda_derivada_evaluada = derivada_segunda.subs(x, punto)
        if segunda_derivada_evaluada.is_positive:
            extremos.append((punto, 'mínimo'))
        elif segunda_derivada_evaluada.is_negative:
            extremos.append((punto, 'máximo'))
    print("===================================");
    print("");
    print("======================================");
    print(".......... MUESTRA DE DATOS ..........")
    print("======================================");
    print(".... La venta es    : ",Venta,"....");
    print(".... El costo es    : ",Costo,"....");
    print(".... La utilidad es : ",Utilidad,"....");
    print(".... La derivada es : ",derivada,"....");
    print("Extremos encontrados:")
    for punto, tipo in extremos:
        print(f" - En x = {punto}, hay un {tipo}")
    print("======================================");
if(Opc == 3):
    print("===================================");
    print("Haz seleccionado salir del programa");
    print("          ¡¡Nos vemos!!            ");
    print("===================================");
    exit;