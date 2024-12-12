#Write a program that converts a decimal number into a binary number.
#To convert a decimal number to binary

# input dziesietnej
decimal_number = int(input("Enter decimal number: "))

# zapisane zeby pokazywac w princie, bo inaczej bedzie zawsze 0
decimal = decimal_number

binary_number = ""



if decimal_number == 0:
    binary_number = "0"
else:
    for x in range(100):  
        if decimal_number == 0: 
            break #ucieczka kiedy dzieisetnia = 0
        remainder = decimal_number % 2  # reszta z dzielenia przez 2
        decimal_number = decimal_number // 2  
        binary_number = str(remainder) + binary_number  # dodawanie reszty na sam poczatek reszte

print(f"{decimal}(10) = {binary_number}(2)")
