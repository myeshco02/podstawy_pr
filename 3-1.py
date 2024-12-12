###
# To use the functions available in an external module,
# you must include that module in your program.
import math

# Pierwiastek kwadratowy z 7
square_root = math.sqrt(7)
print('Pierwiastek kwadratowy z 7 to: ', square_root)

# Logarytm naturalny z 5
logn_5 = math.log(5)
print(f"Logarytm naturalny z 5 to: {logn_5}")

# Sinus 90 stopni
# Konwersja stopni na radiany, ponieważ funkcje trygonometryczne w math działają w radianach
sin_90 = math.sin(math.radians(90))
print(f"Sinus 90 stopni to:  {sin_90}")