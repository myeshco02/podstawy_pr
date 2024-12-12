array = [8,2,5,1,9]

def secPower(x):
    secPowerArray = []
    i =0
    while i < len(x):
        secPowerArray.append(array[i] * array[i])
        i+=1
    return secPowerArray
print(f"Default array: {array} ")
print(f"2nd power of this array {secPower(array)} ")
