def separation(x):
    array=[]
    for i in x:
        if i % 2 == 0:
            array.append(i)
    print(array)
    for i in x:
        if i % 2 == 1:
            array.append(i)
    return array

arr = [7,9,2,4,5,6]

print(separation(arr))
