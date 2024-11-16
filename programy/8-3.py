###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#


while True: #petla sprawdza czy dobra liczba 
    temp_c_str = (input("Podaj temperaturę w stopniach Celsjusza: "))
    temp_c = float(temp_c_str) #konwersja str na float

    if temp_c <= -273.15:
        print("Fizyczka do poprawy! Takiej temperatury nie ma gamoniu") 
        #W przypadku wprowadzenia złej liczby
    else:
        temp_k = temp_c + 273.15 #obliczenie temp w K
        temp_f = temp_c * 9/5 + 32  #obliczenie temp w F
        break



print(f"""Temperatura w Kelwinach: {temp_k: ,.1f} 
Temperatura w Farenheitach: {temp_f: ,.1f}
      """) #wypisanie wyników z dokładnością 1 miejsca po przecinku