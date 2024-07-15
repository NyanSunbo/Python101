import math

# Time Complexity   : O(log n)
# Space Complexity  : O(1)

def binary_search(list, target):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = math.floor((low + high) / 2)
        guess = list[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return None


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))  # => 1
print(binary_search(my_list, 7))  # => 3
print(binary_search(my_list, -1))  # => None
