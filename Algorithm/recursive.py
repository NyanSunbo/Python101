# Recursive function has two part
# First base case
# Second recursive case

def countdown(i):
    if i <= 0:          # <= base case (stop recursive)
        return
    else:               # <= recursive case (do until found condition in base case)
        print(i)
        countdown(i-1)


def factorial(i):
    if i == 1:
        return 1
    else:
        return i * factorial(i-1)


countdown(5) # => 5 4 3 2 1

print(factorial(5)) # => 120
print(factorial(3)) # => 6

#4.1  Write out the code for the earlier sum function
import math


def recursiveSum(arr):
    if arr == []:
        return 0
    return arr[0] + recursiveSum(arr[1:])


print("================ 4.1 ================")
print(recursiveSum([1, 2, 4]))


#4.2 Write a recursive function to count the number of items in a list.

def recursiveCount(arr, n=0):
    if arr == []:
        return 0
    return 1 + recursiveCount(arr[1:])


print("================ 4.2 ================")
print(recursiveCount([1, 2, 3, 4]))


#4.3 Find the maximum number in a list

def recusiveFindMax(arr):
    if len(arr) == 2:
        return max(arr[0], arr[1])
    else:
        return max(arr[0], recusiveFindMax(arr[1:]))

print("================ 4.3 ================")
print(recusiveFindMax([1, 99, 2, 3, 4]))


#4.4 Remember binary search from chapter 1? It’s a divide-and-conquer
#algorithm, too. Can you come up with the base case and recursive
#case for binary search?

def recrusiveBinarySearch(arr, target):
    if len(arr) == 1 and arr[0] == target: print(str(target) + " Found!")
    hi = len(arr)
    lo = 0
    if hi == 1: return
    mid = math.floor((lo + hi) / 2)

    recrusiveBinarySearch(arr[0:mid], target)
    recrusiveBinarySearch(arr[mid:hi], target)



print("================ 4.4 ================")
recrusiveBinarySearch([1, 99, 2, 3, 4], 1)