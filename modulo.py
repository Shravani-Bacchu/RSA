def modulo(a, b):
    a = int(a)
    b = int(b)
    return a % b

def congruence_checker(setofnums):
    x = int(input("Enter a number: "))
    y = int(input("Enter another number (not 0): "))
    while y == 0:
        y = int(input("y cannot be 0. Enter another number: "))
    target = modulo(x, y)

    setofnums = []

    # keep asking until we get a valid (positive) count
    n = int(input("Enter the number of elements in your list: "))
    while n <= 0:
        test = input("That number isn't valid. Try again? Type Y or N: ")
        if test == "Y":
            n = int(input("Enter the number of elements in your list: "))
        else:
            return []  # user gave up, nothing to check

    for i in range(n):
        element = input("Enter a number: ")
        setofnums.append(int(element))
    print(setofnums)

    matches = []
    for i in setofnums:
        if modulo(i, y) == target:
            matches.append(i)
    return matches

sets = [-34, -17, 8, 29, 47]
matches = congruence_checker(sets)
print(matches)

