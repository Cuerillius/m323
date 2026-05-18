def square(lst):
    return [number**2 for number in lst]

print(square(list(range(9))))

def even(lst):
    return [number for number in lst if number % 2 == 0]

print(even(list(range(20))))
