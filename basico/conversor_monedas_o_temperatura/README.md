# Conversor de Monedas y Temperatura

Este proyecto es una aplicación de consola en Python que permite convertir entre monedas (USD/EUR) y temperaturas (Celsius/Fahrenheit) de manera interactiva.

## Descripción

El programa muestra un menú donde el usuario puede elegir entre las siguientes opciones:

1. Convertir de USD a EUR
2. Convertir de EUR a USD
3. Convertir de Celsius a Fahrenheit
4. Convertir de Fahrenheit a Celsius
5. Salir

Cada opción solicita al usuario el valor a convertir, realiza la conversión utilizando funciones auxiliares y muestra el resultado. El programa valida las entradas y permite repetir operaciones hasta que el usuario decida salir.

## Estructura de archivos

- **main.py**  
  Archivo principal que contiene la lógica del menú, la interacción con el usuario y las llamadas a las funciones de conversión.

- **helpers/helpers.py**  
  Módulo auxiliar donde se definen las funciones de conversión:
  - `convert_usd_to_eur(monto)`
  - `convert_eur_to_usd(monto)`
  - `convert_celsius_to_fahrenheit(temp)`
  - `convert_fahrenheit_to_celsius(temp)`
  - Además de utilidades como `clear_screen` y `handle_output_keyboard`.

## Cómo usar

1. Ejecuta el archivo `main.py`.
2. Selecciona la opción deseada del menú (1-5).
3. Ingresa el valor a convertir cuando se solicite.
4. El resultado se mostrará en pantalla.
5. Puedes realizar varias conversiones hasta elegir la opción de salir.

## Ejemplo de uso

```
===================================
         Conversor de Monedas      
===================================
Bienvenido al conversor de monedas y temperatura.
Puedes convertir entre USD y EUR, así como entre Celsius y Fahrenheit.
Selecciona una opción:
1. Convertir de USD a EUR
2. Convertir de EUR a USD
3. Convertir de Celsius a Fahrenheit
4. Convertir de Fahrenheit a Celsius
5. Salir
===================================
Por favor, introduce tu opción (1-5): 1
Introduce la cantidad en USD: 10
10.00 USD son 9.20 EUR
Presiona Enter para continuar...
```

## Notas

- El programa valida que las entradas sean numéricas y muestra mensajes de error si no lo son.
- Para finalizar el programa, selecciona la opción 5 del menú.
- Las tasas de conversión pueden estar definidas en el módulo `helpers`.

---