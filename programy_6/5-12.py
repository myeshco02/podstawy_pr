# Funkcja odwracająca ciąg za pomocą stosu
def reverse_string_with_stack(input_string):
    stack = []  # Tworzenie pustego stosu
    
    # Dodawanie każdego znaku ciągu na stos
    for char in input_string:
        stack.append(char)
    
    # Usuwanie znaków ze stosu i tworzenie odwróconego ciągu
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

# Program główny
if __name__ == "__main__":
    user_input = input("Wprowadź ciąg, który chcesz odwrócić: ")
    reversed_result = reverse_string_with_stack(user_input)
    print("Odwrócony ciąg:", reversed_result)
