from hidecardnumber import hide

# Numer karty kredytowej
card_number = input("Enter a 16-digit credit card number: ")

try:
    masked_card = hide(card_number)
    print(f"Masked card number: {masked_card}")
except ValueError as e:
    print(e)
