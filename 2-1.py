###
# Program for testing built-in functions
#

# Największa liczba w liście [7, 5, 6, 3, 8, 2]
max_number = max(7,5,6,3,8,2)
print('Największa liczba z 7,5,6,3,8,2 to', max_number)

# Najmniejsza liczba w liście [4, 7, 2, 3, 9, 8]
min_number = min(4,7,2,3,9,8)
print('Najmniejsza liczba z 4,7,2,3,9,8 to', min_number)

# Długość frazy "informatyka"
str_length = len("computer science")
print('Długość frazy "computer science" to', str_length)

# Litera wprowadzona z klawiatury
letter = input("Wpisz pojedynczą literę: ")
    # Pętla dla upewnienia się, że litera jest pojedyncza
if len(letter) == 1 and letter.isalpha():
    print(f"Wpisałeś literę: {letter}")
else:
    print("Nieprawidłowa wartość. Wpisz pojedynczą literę.")

# Liczba reprezentująca ciąg "20303"
number_from_string = int("20303")
print(f"Liczba reprezentująca ciąg '20303': {number_from_string}")

# Ciąg binarny reprezentujący liczbę dziesiętną 304
binary_representation = bin(304)
print(f"Ciąg binarny reprezentujący liczbę dziesiętną 304: {binary_representation}")

# Ciąg szesnastkowy reprezentujący liczbę dziesiętną 304
hex_representation = hex(304)
print(f"Ciąg szesnastkowy reprezentujący liczbę dziesiętną 304: {hex_representation}")

# Liczba całkowita reprezentująca kod Unicode znaku €
unicode_code = ord("€")
print(f"Liczba całkowita reprezentująca kod Unicode znaku €: {unicode_code}")

# Wartość bezwzględna -17
absolute_value = abs(-17)
print(f"Wartość bezwzględna z -17: {absolute_value}")
