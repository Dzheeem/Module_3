data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(stucture):
    total = 0
    if isinstance(stucture, (int, float)):
        return stucture
    elif isinstance(stucture, dict):
        for key, values in stucture.items():
            total += calculate_structure_sum(len(key))
            total += calculate_structure_sum(values)
    elif isinstance(stucture, (tuple, list, set)):
        for items in stucture:
            total += calculate_structure_sum(items)
    elif isinstance(stucture, str):
        for words in stucture:
            total += calculate_structure_sum(len(words))
    return total

print(calculate_structure_sum(data_structure))