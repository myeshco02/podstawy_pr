n = int(input('Type any integer: '))


for x in range(n):
    if x > 1:  #Liczby pierwsze są większe od 1
        for y in range (2, x): # Sprawdza wszystkie dzielniki w zakresie od 2 do x-1
            if (x % y) == 0: 
                break # jezeli x jest podzielne przez y wtedy liczba nie jest liczbą pierwszą
        else:
            print(x, end=' ')
