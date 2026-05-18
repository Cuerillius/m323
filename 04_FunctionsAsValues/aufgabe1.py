# Aufgabe 1
def doubleNumber(lst):
    return list(map(lambda item: item * 2, lst))

print(doubleNumber([1,2,3,4,5,6,8,9]))

# Aufgabe 2
def listToUppercase(lst):
    return list(map(lambda item: item.upper(), lst))

print(listToUppercase(["Alice", "Bob", "Charlie"]))