###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = float(input('Wpisz dowolną liczbe: '))
number2 = float(input('Wpisz drugą dowolną liczbe: '))
operator = input('Wpisz operator +, -, *, /:' )

if operator == '+':
    result = number1+number2
elif operator == '-':
    result = number1-number2
elif operator == '*':
    result = number1*number2
elif operator == '/':
    if number2 !=0:
        result = number1/number2
    else:
        print('Nie mozesz dzielic przez 0')
else:
    print('Wprowadziles zly operator')

# print result
print(f'{number1} {operator} {number2} = {result}')
