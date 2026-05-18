# Aufgabe 1

def remove_odd(lst: list[int]):
    return list(filter(lambda x: x %2 == 0, lst))
    
print(remove_odd([1,2,3,4,5]))

# Aufgabe 2

def select_more_than_four(lst: list[str]):
    return list(filter(lambda x : len(x) > 4, lst))

print(select_more_than_four(["Alice", "Bob", "Charlie", "Diana"]))