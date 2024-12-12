import random

def rand(x):
    for i in range(5):
        print(x[random.randint(0, len(x)-1)]) #prints a value from array using random index from range 0 to lengh of array 
        
arr = [9, 7, 3, 2, 1]
print(rand(arr))
