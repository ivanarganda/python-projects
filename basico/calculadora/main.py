import sys
from helpers.helpers import *

def main():

    num1 = input("Enter the first number: ")
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = input("Enter the second number: ")

    result = calculate(num1, operator, num2)  

    print(f"Result: {result}")

if __name__ == "__main__":
    main()