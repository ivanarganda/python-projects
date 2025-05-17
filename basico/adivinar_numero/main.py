import sys
import signal
from helpers.helpers import *

def display_game_status(history, min, max, attempts):
    clear_screen()
    print("\n=== ADIVINA EL NÚMERO ===")
    print(f"Rango actual: {min} - {max}")
    print(f"Intentos restantes: {attempts}")
    
    if history:
        print("\nHistorial de intentos:")
        for i, (num, result) in enumerate(history, 1):
            print(f"{i}. Número {num}: {result}")
    print("\n" + "="*23 + "\n")

def main():
    """
    Main game function that implements a number guessing game.
    The game allows players to guess a random number between 1 and 100 within 5 attempts.
    It provides feedback after each guess indicating if the target number is higher or lower.
    The game keeps track of previous guesses and updates the valid number range accordingly.
    Game Rules:
    - Player has 5 attempts to guess the correct number
    - Valid number range is between 1-100 
    - Enter 0 to quit the game at any time
    - Invalid inputs do not count as attempts
    Returns:
        None
    Raises:
        ValueError: If input cannot be converted to integer
        SystemExit: If player enters 0 to quit game
    Example:
        >>> main()
        Bienvenido al juego de adivinar el número
        Tienes 5 intentos para adivinar el número entre 1 y 100
        ...
    """
    print("Bienvenido al juego de adivinar el número")
    print("Tienes 5 intentos para adivinar el número entre 1 y 100")
    print("Si quieres salir, escribe '0' en cualquier momento")

    number_to_guess = get_random_number()
    min = 1
    max = 100
    attempts = 5
    history = []

    while attempts > 0:
        try:
            display_game_status(history, min, max, attempts)
            number = int(handle_output_keyboard(signal, f"Por favor, introduce un número entre {min} y {max}: "))
            
            if number == -1:
                continue
            if number == 0:
                print("Gracias por jugar. ¡Hasta luego!")
                sys.exit(0)

            if number < number_to_guess:
                result = "El número es mayor ⬆️"
                attempts -= 1
                min = number
                history.append((number, result))
            elif number > number_to_guess:
                result = "El número es menor ⬇️"
                attempts -= 1
                max = number
                history.append((number, result))
            else:
                display_game_status(history, min, max, attempts)
                print("🎉 ¡Felicidades! Has adivinado el número 🎉")
                return

        except ValueError as e:
            print(e)
            continue

    display_game_status(history, min, max, attempts)
    print(f"❌ Game Over. El número era {number_to_guess}")

if __name__ == "__main__":
    main()