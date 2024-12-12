# keyboard.py

def input_string(message):
    #Zwraca ciąg znaków wprowadzony z klawiatury
    value = input(message)
    return value

def input_integer(message):
    #Zwraca liczbę całkowitą wprowadzoną z klawiatury
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("Please enter a valid integer.")

def input_real(message):
    #Zwraca liczbę rzeczywistą wprowadzoną z klawiatury
    while True:
        try:
            value = float(input(message))
            return value
        except ValueError:
            print("Please enter a valid number.")

def input_boolean(message):
    #Zwraca wartość logiczną w zależności od naciśniętego klawisza y/n
    while True:
        choice = input(message).strip().lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'.")