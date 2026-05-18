def flatten_and_multiply_list(big_lst: list[list[int]]):
    return [number*2 for lst in big_lst for number in lst]

print(flatten_and_multiply_list([[1,2],[3,4]]))

def flatten_and_filter_unique(big_lst: list):
    return set([name for _, lst in big_lst for name in lst])

print(flatten_and_filter_unique([("Max", ["Blau", "Grün"]), ("Anna", ["Rot"]), ("Julia", ["Gelb", "Blau", "Grün"])]))