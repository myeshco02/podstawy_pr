#Write a program that prints numbers from 1 to 30.
#If the number is divisible by 3 then the program prints the word 'THREE'.
#Next, if the number is divisible by 5
#then the program prints the word 'FIVE'.
#Finally, if the number is divisible by both 3 and 5
#then the program prints the word 'BINGO'

for x in range(1, 31):
    if x % 3 == 0 and x % 5 == 0:
        print('BINGO', end=' ')  #end dodane zeby byly w tej samej linii
    elif x % 3 == 0:
        print('THREE', end=' ')
    elif x % 5 == 0:
        print('FIVE', end=' ')
    else:
        print(x, end=' ')
