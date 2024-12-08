#Write a program that creates a multiplication table in
#the range 1 to 10 for any number entered by the user.

number = int(input('Enter a number: '))
for x in range (1, 11):
    print(number, 'x', x, '=', number*x)
