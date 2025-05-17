def calculate(number):
    pass

def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def get_random_number():
    import random
    return random.randint(1, 100)

def handle_output_keyboard(signal, prompt_text):
    try:
        choice = input(prompt_text)
        return choice
    except KeyboardInterrupt:
        return -1