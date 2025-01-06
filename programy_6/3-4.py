import queue

def decimal_to_binary(n):
    # Tworzymy stos
    stack = queue.LifoQueue()
    
    # Dzielimy liczbę przez 2 i zapisujemy resztę na stosie
    while n > 0:
        remainder = n % 2  # Reszta z dzielenia przez 2 (0 lub 1)
        stack.put(remainder)
        n = n // 2  # Dzielenie przez 2 (całkowite)
    
    # Wyciągamy i drukujemy cyfry binarne w odwrotnej kolejności
    binary_number = ''
    while not stack.empty():
        binary_number += str(stack.get())
    
    return binary_number

# Przykład konwersji liczby
number = 18
print(f"Natural number: {number}")
binary = decimal_to_binary(number)
print(f"Binary number: {binary}")
