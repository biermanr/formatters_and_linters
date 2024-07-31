from math import prod


def add_to_list(*elements, starting_list=[]):
    starting_list.extend(elements)
    return starting_list


def sylvester(n):
    sequence = add_to_list(2)
    for _ in range(n - 1):
        new_num = 1 + prod(sequence)
        sequence = add_to_list(new_num, starting_list=sequence)
    return sequence


print(sylvester(2))
print(sylvester(3))
print(sylvester(4))
