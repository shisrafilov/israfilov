x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def find_even(list_of_numbers):
    result = []
    for i in list_of_numbers:
        if i % 2 == 0:
            result.append(i)
    return result


print(find_even(x))
