# Importamos las bibliotecas necesarias
import sys  # Para funciones del sistema, como salir del programa
import signal  # Para manejar señales del sistema operativo
from helpers.helpers import *  # Importamos todas las funciones auxiliares del módulo helpers

def main():
    """
    Función principal que ejecuta el conversor de monedas y temperatura.
    Muestra un menú interactivo y maneja las diferentes conversiones.
    """
    while True:  # Bucle principal del programa
        # Limpiamos la pantalla para mejor visualización
        clear_screen()        
        
        # Mostramos el menú principal con todas las opciones
        print("===================================")
        print("         Conversor de Monedas      ")
        print("===================================")
        print("Bienvenido al conversor de monedas y temperatura.")
        print("Puedes convertir entre USD y EUR, así como entre Celsius y Fahrenheit.")
        print("Selecciona una opción:")
        print("1. Convertir de USD a EUR")
        print("2. Convertir de EUR a USD")
        print("3. Convertir de Celsius a Fahrenheit")
        print("4. Convertir de Fahrenheit a Celsius")
        print("5. Salir")
        print("===================================")
        
        try:
            # Capturamos la opción del usuario con manejo de señales del teclado
            choice = int(handle_output_keyboard(signal, "Por favor, introduce tu opción (1-5): "))
            if choice == -1:  # Si se detecta una señal de interrupción
                continue
                
            if choice == 1:  # Opción: Conversión de USD a EUR
                try:
                    amount = float(input("Introduce la cantidad en USD: "))
                    result = convert_usd_to_eur(amount)  # Llamamos a la función de conversión
                    print(f"{amount:.2f} USD son {result:.2f} EUR")
                    input("Presiona Enter para continuar...")
                    continue
                except ValueError:  # Manejo de error si el input no es un número
                    print("Error: Por favor, introduce un número válido.")
                    input("Presiona Enter para continuar...")
                    continue
                    
            elif choice == 2:  # Opción: Conversión de EUR a USD
                try:
                    amount = float(input("Introduce la cantidad en EUR: "))
                    result = convert_eur_to_usd(amount)  # Llamamos a la función de conversión
                    print(f"{amount:.2f} EUR son {result:.2f} USD")
                    input("Presiona Enter para continuar...")
                except ValueError:  # Manejo de error si el input no es un número
                    print("Error: Por favor, introduce un número válido.")
                    input("Presiona Enter para continuar...")
                    continue
                    
            elif choice == 3:  # Opción: Conversión de Celsius a Fahrenheit
                try:
                    amount = float(input("Introduce la temperatura en Celsius: "))
                    result = convert_celsius_to_fahrenheit(amount)  # Llamamos a la función de conversión
                    print(f"{amount}°C son {result}°F")
                    input("Presiona Enter para continuar...")
                    continue
                except ValueError:  # Manejo de error si el input no es un número
                    print("Error: Por favor, introduce un número válido.")
                    continue
                    
            elif choice == 4:  # Opción: Conversión de Fahrenheit a Celsius
                try:
                    amount = float(input("Introduce la temperatura en Fahrenheit: "))
                    result = convert_fahrenheit_to_celsius(amount)  # Llamamos a la función de conversión
                    print(f"{amount}°F son {result}°C")
                    input("Presiona Enter para continuar...")
                    continue
                except ValueError:  # Manejo de error si el input no es un número
                    print("Error: Por favor, introduce un número válido.")
                    continue
                    
            elif choice == 5:  # Opción: Salir del programa
                print("Gracias por usar el conversor de monedas. ¡Hasta luego!")
                sys.exit(0)  # Terminamos el programa con código de salida 0 (exitoso)
                
            else:  # Si se introduce una opción fuera del rango 1-5
                print("Opción no válida. Por favor, selecciona una opción válida.")
                
        except ValueError:  # Manejo de error si la opción no es un número
            print("Error: Por favor, introduce una opción válida (1-5).")

# Punto de entrada del programa
if __name__ == "__main__":  # Verifica si el script se está ejecutando directamente
    main()  # Llama a la función principal