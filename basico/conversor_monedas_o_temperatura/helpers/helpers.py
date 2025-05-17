def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def handle_output_keyboard(signal, prompt_text):
    try:
        choice = input(prompt_text)
        return choice
    except KeyboardInterrupt:
        return -1

def convert_usd_to_eur(amount):
    """
    Convert USD to EUR.
    """
    conversion_rate = 0.85  # Example conversion rate
    return amount * conversion_rate

def convert_eur_to_usd(amount):
    """
    Convert EUR to USD.
    """
    conversion_rate = 1 / 0.85  # Example conversion rate
    return amount * conversion_rate

def convert_celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    """
    return (celsius * 9/5) + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    """
    return (fahrenheit - 32) * 5/9