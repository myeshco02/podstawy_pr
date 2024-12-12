from binary import is_binary

# Wprowadzenie liczby binarnej
binary_number = input("Enter a binary number: ")

if is_binary(binary_number):
    print(f"{binary_number} is a valid binary number.")
else:
    print(f"{binary_number} is not a valid binary number.")
