###
# A program that calculates the length of the diagonal
# of a rectangle with sides a and b.
#
import math
a = 5
b = 8
diagonal = math.sqrt(a**2 + b**2)
print('Przekątna tego prostokąta wynosi:', diagonal)
print('Przekątna tego prostokąta (w przyblizeniu) wynosi:', round(diagonal, 5))
#zaokraglone do 5 miejsc po przecinku