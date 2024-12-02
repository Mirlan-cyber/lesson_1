data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data_structure):
    result = 0
    for item in data_structure:
        if isinstance(item, int):
            result += item
        elif isinstance(item, str):
            result += len(item)
        elif isinstance(item, dict):
            for key, value in item.items():
                if isinstance(key, str):
                    result += len(key)
                if isinstance(value, int):
                    result += value
        elif isinstance(item, tuple) or isinstance(item, list) or isinstance(item, set):
            result += calculate_structure_sum(item)
    return result


result = calculate_structure_sum(data_structure)
print(result)
