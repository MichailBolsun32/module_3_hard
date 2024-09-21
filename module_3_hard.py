def calculate_structure_sum(*data_structure):
    sum_ = 0
    for arg in data_structure:
        if isinstance(arg, bool):  # Проверка на bool, сиходим в подсчете из того, что bool значение = str
            if arg:
                sum_ += 4
            else:
                sum_ += 5
        elif isinstance(arg, (int, float)):  # Проверка на числа
            sum_ += arg
        elif isinstance(arg, str):  # Проверка на строку
            sum_ += len(arg)
        elif isinstance(arg, (list, tuple, set)):  # Проверка на списки, картеджи, множества
            sum_ += calculate_structure_sum(*arg)
        elif isinstance(arg, dict):
            arg = arg.items()
            sum_ += calculate_structure_sum(*arg)
    return sum_


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

sum_ = calculate_structure_sum(data_structure)
print(sum_)
