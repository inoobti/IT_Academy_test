unsorted_list = [2, 5, 7, 4, 3, 5, 2, 1, 7, 7, 4, 6, 1, 5, 3, 6, 7, 5, 6, 6]


def check(check_list):
    for num in check_list:
        if isinstance(num, int):
            return True


def sort_list_1(l):
    if check(l):
        return list(set(l))
    else:
        raise ValueError("Передаваемый список должен содержать только целые числа")


print(sort_list_1(unsorted_list))


def sort_list_2(l):
    new_list = []
    if check(l):
        for num in l:
            if num in new_list:
                continue
            else:
                new_list.append(num)
        return sorted(new_list)
    else:
        raise ValueError("Передаваемый список должен содержать только целые числа")


print(sort_list_2(unsorted_list))