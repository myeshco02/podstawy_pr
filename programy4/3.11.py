arr1 = [6,2,7,21,9,1,5]
arr2 = [156, 6346, 432,1, 4326]

def bubbleSort(arr):
   n = len(arr)
   for i in range (n-1):
      for j in range (n-i-2):
         if arr[j] > arr[j+1]:
               arr[j], arr[j + 1] = arr[j + 1], arr[j]
   return arr

sortedArr1 = bubbleSort(arr1[:])
sortedArr2 = bubbleSort(arr2[:])

print(sortedArr1)
print(sortedArr2)
