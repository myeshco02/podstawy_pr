###
# Calculates arithmetic mean of two integer numbers
#
def mean(x,y):
   mean = sum((x, y)) / 2
   return mean

# takes two numbers from keyboard
n1 = float(input('Enter the first number: '))
n2 = float(input('Enter the second number: '))

# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')