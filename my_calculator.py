#!/usr/bin/env python

def welcome_message(message):
    print(message)

def goodbye():
    print("\nGoodbye, then... \U0001F984")
    print("***" * 10)

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else None
}

def perform_operation(choice, a, b):
    return operations.get(choice, lambda a, b: None)(a, b)

welcome_message("Welcome to the calculator")

def play():
    a = float(input(""))

    choice = input("Proceed with your operation: ")

    if choice == "q":
        goodbye()
        return False

    b = 0
    while b == 0:
        b = float(input(""))
        if b == 0:
            print("You can't divide by zero, you twat. Try again")

    if choice in operations:
        result = perform_operation(choice, a, b)
        if result is not None:
            print(f"Result: {result}" if result is not None else "Error")
        else:
            print("Error")
    else:
        print("Invalid entry")

    return True

if __name__ == "__main__":
    while play():
        pass
