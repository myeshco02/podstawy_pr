arr=[1,2,3,4,5]

#original array
print('Original array',arr)

#substracting 1 from first value
arr[0]=arr[0]-1
print(arr)

#increasing last element by 4
arr[-1]=arr[-1]+4
print(arr)

#multiplying middle item by 2
mid=len(arr)//2
arr[mid]=arr[mid]*2
print(arr)
