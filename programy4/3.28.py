arr=[
    [7,3,7,9,0],
    [2,9,0,1,5],
    [3,8,6,4,7],
    [8,7,1,1,5]
]

def lastRow(x):
    return sum(row[len(x)] for row in arr)
    
print(lastRow(arr))
