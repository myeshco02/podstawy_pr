arr = [3.51, 12.5, 4.1, 1.01]

def higherNum(x, arr):
    count = 0
    for i in arr:
        if x > i:
            count+=1
    return count
    
number =int(input("Podaj liczbe: "))
print(f"{higherNum(number, arr)} smaller numbers than {number} ")
