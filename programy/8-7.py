#binary and hex converter from integer

number = int(input("Enter number: "))

bin_number = bin(number)
hex_number = hex(number)

print(f"Binary number: {bin_number}")
print(f"Hexadecimal number: {hex_number}")

#UWAGA
#LICZBY W OUTPUCIE POPRZEDZONE SĄ PREFIXAMI 
# 0b dla binary
# 0x dla szesnastkowego

#służą określeniu systemu
#dziesiętny nie ma prefixu (domyślny system)

#jeśli chcemy się pozbyć prefixu używamy slicingu czyli dodajemy [2:]
#przykład:
#binary_number = bin(number)[2:] 