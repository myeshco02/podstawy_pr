def secLargest(x): #function that check for second largest item
    if len(x) < 2: #if checking is the array bigger than 2
        return None
        
    first, sec = float("-inf"), float("-inf") #-inf is negative infinity. This guarantees us the first number we check will be higher than these
    for i in x:
        if i > first:
            sec = first
            first = i #if the number is higher than first we place its value to first and second
        elif i > sec and i != first:
            sec = i #if number is not higher than first but bigger than second we replace second value with number
    return sec
   
def diffMaxMin(x):
    Max = max(x)
    Min = min(x)
    
    dif = Max - Min
    return dif
    
def median(x):
    #sorting the array
    x.sort()
                
    index = len(x) // 2 # finding the middle index
    median = x[index] #asigining middle index value (median) to a variable
    return median
    
def MinMax(x):
    smallArr=[]
    smallArr.append(max(x))
    smallArr.append(min(x))
    return smallArr
    
def arrString(x):
    return "-".join(str(i) for i in x)
arr = [7,3,8,5,2]
arrCopy = arr.copy()
print(f"The array is: {arr} ")
print(f"Second largest: {secLargest(arr)} ")
print(f"Difference between Max and Min value: {diffMaxMin(arr)} ")
print(f"Median is {median(arrCopy)} ")
print(f"Max and min value: {MinMax(arr)} ")
print(f"Array as string: {arrString(arr)} ")
