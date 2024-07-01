
####### Cod CHATGPT #########
from os import system 
#import numpy as np
#from scipy.optimize import minimize
system("cls");
print("");
print(".... Bienvenido....");
print("");
print("=================================")
print(".... Menu ....");
print("=================================");
print("  1.- Calcular la Utilidad  ");
print("  2.-  Salir del Programa  ");
print("  3.-     ");
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
if(Opc == 1):
    print("===============================================");
    print(".... Haz seleccionado Calcular la Utilidad ....");
    print("===============================================");
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
            
if(Opc == 2):
    print("===================================");
    print("Haz seleccionado salir del programa");
    print("          ¡¡Nos vemos!!            ");
    print("===================================");
    exit;