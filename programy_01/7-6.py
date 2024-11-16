speed = float(input('Podaj prędkość: '))
speed_ok = speed in range(40, 140)
print(f'Speed is valid: {speed_ok}')