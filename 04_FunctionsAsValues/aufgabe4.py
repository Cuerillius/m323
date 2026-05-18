from functools import reduce

def calculate_sum(lst: list[int]):
    return reduce(lambda a,b : a+b, lst)

print(calculate_sum([1,2,3,4,5]))

def add_together(lst: list[str]):
    return reduce(lambda a,b : a+b, lst)
    
print(add_together(["Hallo", " ", "Welt", "!"]))