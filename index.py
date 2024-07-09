from os import system 
import math
import sympy as sp 
#import numpy as np
while True:
    system("cls");
    print("");
    print("=======================================");
    print(".... Bienvenido a nuestro programa ....");
    print("=======================================");
    print("");
    print("=================================")
    print(".... Menu de Calculos ....");
    print("=================================");
    print("  1.-  Calcular la Utilidad  ");
    print("  2.-  Calcular Utilidad Maxima  ");
    print("  3.-  Salir del Programa   ");
    print("=================================");
    print("");
    Opc = None  # Inicializamos Opc con None para asegurar que entre al bucle la primera vez
    while Opc not in [1, 2, 3]:  # Mientras Opc no sea 1 o 2, repetir la solicitud
        try:
            Opc = int(input("Ingrese opción (1-3): ").strip())  # Pedimos la opción y la convertimos a entero
            if Opc not in [1, 2, 3]:  # Si la opción no está en el rango deseado, mostrar mensaje de error
                print("Por favor ingrese una opción válida (1-3)")
        except ValueError:  # Si no se puede convertir a entero, mostrar mensaje de error
            print("Por favor ingrese una opción válida (1-3)")
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
                    raise ValueError("No ha ingresado ningún valor");
                x = float(Valor1)  # Intentamos convertir el valor a un número flotante
                while x < 0 or x == 0: # Si el usuario inserta valores negativos o 0
                    Valor1 = input("¡¡¡No ingrese valores menjores a 0 o negativos!!!: ").strip()
                    x = float(Valor1)
                # Si llegamos hasta aquí, hemos obtenido con éxito un número
                break  # Salimos del bucle while porque tenemos el valor correcto
            except ValueError as e:
                print(f"Error: {e}. Por favor ingrese un número válido.");
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
        derivada = sp.diff(Utilidad, x)

        # Solucionar la derivada para encontrar los puntos críticos
        puntos_criticos = sp.solve(derivada, x)

        # Evaluar la Utilidad en los puntos críticos y en los extremos del dominio (si existen)
        utilidad_en_puntos = [(punto, Utilidad.subs(x, punto)) for punto in puntos_criticos]
        extremos = puntos_criticos + [(0,), (sp.oo,)]  # Agregar extremos del dominio
        for punto, utilidad in utilidad_en_puntos:
            print(f'Punto crítico: x = {punto}')
        # Mostrar resultados
        print("===================================");
        print("");
        print("======================================");
        print(".......... MUESTRA DE DATOS ..........")
        print("======================================");
        print(".... La venta es    : ",Venta,"....");
        print(".... El costo es    : ",Costo,"....");
        print(".... La utilidad es : ",Utilidad,"....");
        print(".... La derivada es : ",derivada,"....");
        print(".... La Utilidad maxima es : ",punto,"....");
        print("======================================");
    if(Opc == 3):
        print("===================================");
        print("Haz seleccionado salir del programa");
        print("          ¡¡Nos vemos!!            ");
        print("===================================");
        break;
    continuar = input("\n¿Desea realizar otra operación? (s/cualquier tecla): ").strip().lower()
    if continuar != 's':
        break  # Salir del bucle principal si la respuesta no es 's'