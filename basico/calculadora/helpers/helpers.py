def calculate(num1, operator, num2):
    try:
        if num1 == "" or num2 == "":
            raise ValueError("No pueden estar vacíos los números")
        if operator not in ['+', '-', '*', '/']:
            raise ValueError("Operador no válido. Debe ser uno de +, -, *, /")
        if operator == '+':
            return float(num1) + float(num2)
        elif operator == '-':
            return float(num1) - float(num2)    
        elif operator == '*':
            return float(num1) * float(num2)
        elif operator == '/':
            if float(num2) != 0:
                return float(num1) / float(num2)
            else:
                return "No se puede dividir por cero"
        else:
            return f"Unknown operator: {operator}"
    except ValueError as e:
        return f"Invalid input: {e}"
