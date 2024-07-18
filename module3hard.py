def calculate_structure_sum(data_structure):
    sum = 0
    i = 0
    if isinstance(data_structure, int):
      sum = sum + data_structure
      return sum
    elif isinstance(data_structure, str):
      sum = sum + len(data_structure)
      return sum
    elif isinstance(data_structure, list) or isinstance(data_structure, tuple):
      i = 0
      while i < len(data_structure):
        sum = sum + calculate_structure_sum(data_structure[i])
        i += 1
      return sum
    elif isinstance(data_structure, set):
        while i < len(data_structure):
            sum = sum + calculate_structure_sum(data_structure.pop())
        return sum
    elif isinstance(data_structure, dict):
      for key, value in data_structure.items():
        sum = sum + calculate_structure_sum(key) + calculate_structure_sum(value)

    return sum


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(calculate_structure_sum(data_structure))


