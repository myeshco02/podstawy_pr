arr1 = ["water","book","sky"]
arr2 = ["water","book","sky"]
arr3 = [3,2,1]
arr4 = [3,2]

def compare(x,y): #function that compares arrays and gives true when they are equal
    return x == y
def cleanerArr(array):
    return " ".join(str(el) for el in array) #function that makes a string separeted with spaces from all array elements

def test(array1, array2):
    print(f"First array: {cleanerArr(array1)} ")  #prints both tested arrays
    print(f"Second array: {cleanerArr(array2)} ")
    if compare(array1, array2): #if arrays are equal this if returns true 
        print("Arrays are equal")
    else:
        print("Arrays are different")
test(arr1, arr2)
print("") #blank line for clarity
test(arr3,arr4)
