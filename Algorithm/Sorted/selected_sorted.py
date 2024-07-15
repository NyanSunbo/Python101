# Time Complexity   : O(n^2)
# Space Complexity  : O(1)


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr



def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range (1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

print(selectionSort([5, 3, 6, 2, 10]))
print(selectionSort([15, 99, 1, 25, 10]))
