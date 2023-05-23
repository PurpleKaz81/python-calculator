#!/usr/bin/env python3.9

def print_message(message):
    print(f"\n{message}\n")

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return print_message("You can't divide by zero!") if b == 0 else a / b

def goodbye():
    print("\nGoodbye, then... \U0001F984")
    print_message("***" * 10)

def display_menu():
    print_message("Welcome to the calculator.")

def operation(choice, a, b):
    if choice == 1:
        return addition(a, b)
    elif choice == 2:
        return subtraction(a, b)
    elif choice == 3:
        return multiplication(a, b)
    elif choice == 4:
        return division(a, b)

def play():
    while True:
        display_menu()
        choice = input("Please select the operation: [1] to add, [2] to subtract, [3] to multiply, [4] to divide, or [q] to bugger off: ")

        if choice == "q":
            goodbye()
            return False

        try:
            choice = int(choice)
            if choice < 1 or choice > 4:
                raise ValueError()
            print()
            a = float(input(""))
            print()
            b = float(input(""))
            result = operation(choice, a, b)
            print(f"\nResult: {result}")
        except ValueError:
            print_message("Invalid Choice! Choose a number between 1-4 or q to quit.")

if __name__ == "__main__":
    play()
