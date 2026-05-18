from functools import cmp_to_key

# Aufgabe 3.1
def calculateSum(list):
    total = 0
    for n in list:
        total += n
    return total

# Aufgabe 3.2
def calculateAverage(list):
    if not list:
        return 0
    return calculateSum(list) / len(list)

# Aufgabe 3.3
def sortAlphabetically(list):
    return sorted(list)

# Aufgabe 3.4

def customSort(a,b):
    if a[0] > b[0]:
        return 1
    if a[1] > b[1]:
        return 1
    if a[2] > b[2]:
        return 1
    return -1

customSortKey = cmp_to_key(customSort)

def sortList(list):
    listToSort = list.copy()
    listToSort.sort(key=customSortKey)
    return listToSort

#Aufgabe 3.5
def countLeaves(branch):
    leaves = 0
    if branch[1]:
        leaves = countLeaves(branch)
    return branch[0] + leaves
    

print("--- Aufgabe 3.1: calculateSum ---")
print(f"Test 1 (Positive): {calculateSum([1, 2, 3, 4, 5])}")
print(f"Test 2 (Mixed):    {calculateSum([-10, 5, 10])}")   
print(f"Test 3 (Empty):    {calculateSum([])}")           

print("\n--- Aufgabe 3.2: calculateAverage ---")
print(f"Test 1 (Standard): {calculateAverage([10, 20, 30])}")
print(f"Test 2 (Single):   {calculateAverage([5])}")       
print(f"Test 3 (Empty):    {calculateAverage([])}")          

print("\n--- Aufgabe 3.3: sortAlphabetically ---")
print(f"Test 1 (Names):    {sortAlphabetically(['Zebra', 'Apple', 'Mango'])}") 
print(f"Test 2 (Case):     {sortAlphabetically(['b', 'a', 'c'])}")

print("\n--- Aufgabe 3.4: sortList ---")
print(sortList([
    ("2023-01-01", 1, "Alpha"),
    ("2023-12-31", 5, "Omega"),
    ("2023-12-31", 10, "Beta")
]))
print(sortList([("2023-05-05", 2, "Task B"), ("2023-05-05", 5, "Task A")]))

print(countLeaves([5, [3, [2, None]]]))