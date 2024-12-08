#n one of the online stores, a 25% discount is
#charged for each product purchased over two.
#Write a program that calculates the amount to be paid.
#Read the number of purchased products
#and the product price from the keyboard.

number = float(input('How many products have you purchased?: '))
price = float(input('What is the price of product?: '))

if number > 2:
    payment = 2 * price
    discount = (number - 2) * price * 0.75
    payment += discount
else:
    payment = price

print(f'Amount to pay: {payment}')
