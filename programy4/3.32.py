arr = [
    [1, 2, 3, 4, 5], #arr[0]
    [6, 7, 8, 9, 10], #arr[1]
    [11, 12, 13, 14, 15] #arr[2]
]

print("Entry array: ")
for row in arr:
    print(row)
    
arr[0], arr[2] = arr[2],arr[0] #swapping first row (index 0) with last row (index)

print("")
print("Array after swapping rows: ")
for row in arr:
    print(row)
