import random

arr1 = [3,7,1,0,4]
arr2 = [[2,3],[7,1],[0,4]]
arr3 = [7 for i in range(5)]
arr4 = [i for i in range(1,10)]
arr5 = [i*2 for i in range(1,10)]
arr6 = [random.randint(1,20) for i in range(10)]
arr7 = [[] for i in range(5)]
arr8 = [[1 for i in range(2)] for j in range(4)]
arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]
#an array with values: 4,0,3
arr10 = [4,0,3]
#15-element array filled with zeros
arr11 = [0 for i in range(15)]
#an array with integer values in the range of <1,30>
arr12 = [i for i in range(1, 31)]
#20-element array filled with 0 or 1 randomly
arr13 = [random.randint(0,1) for i in range(20)]
#two dimensional array with five rows and two columns filled with False
arr14 = [[False] * 2 for _ in range(5)]


#Small additional project with automated printing 
arrays = {} #empty dictionary to fill automatically
for i in range(1,14):
    arrName = f"arr{i}" #generates names for dictionary
    arrays[arrName] = globals()[arrName] #assigns avlues to newly created names and adds them to dictionary

#function printing arrays with consideration of their format 
def printArrs(arrays):
    for name, array in arrays.items(): #for loop for every item in"arrays" dictionary
        print(f"\n{name}:") #prints name of current array
        if isinstance(array[0], list): #isinstance checks if first element in brackets is considered as element after coma (in this example if array[0] is a list, if yes if value is true
            for row in array: #prints 2D arrays
                print(row)
        else:
            print(array) #prints 1D arrays
                
printArrs(arrays)
