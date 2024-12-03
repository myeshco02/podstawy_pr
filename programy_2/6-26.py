#The payment card is secured with a four-digit PIN code (0805).
#Write a program that checks if the PIN code
#entered in the payment terminal is correct.
#The user has up to three possibilities for entering a PIN code.
#In case of three unsuccessful attempts, the card is blocked.

pin_code = "0805"


for i in range(3):
    pin = input("Enter the PIN code: ")
    if pin == pin_code:
        print("Access granted.")
        break  
    else:
        print("Incorrect...")

if pin != pin_code:
    print("Sorry, your payment card has been blocked.")
