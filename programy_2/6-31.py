#Write a program that prints 20
#integer random numbers in the range of 5 to 10.

import random #importuje moduł random
for x in range(20):
    print(random.randint(5, 10), end=' ') # zwraca pseudolosową liczbe z zakresu 5-10)
