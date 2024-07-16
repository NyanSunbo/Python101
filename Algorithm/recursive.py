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