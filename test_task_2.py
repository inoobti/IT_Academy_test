#define arrays
a = [5, 34]
b = [17, 2]


def check(check_list):
    for num in check_list:
        if not isinstance(num, int):
            return True

def cos_angle(vect_1, vect_2):
    if len(vect_1) != len(vect_2):
        raise ValueError(f"Невозможно расчитать при разной длинне векторов. \n "
                         f"длинна вектора {vect_1} = {len(vect_1)}, длинна вектора {vect_2} = {len(vect_2)}")
    elif check(vect_1):
        raise ValueError(f"Не все элементы списка {vect_1} являются целыми числами")
    elif check(vect_2):
        raise ValueError(f"Не все элементы списка {vect_2} являются целыми числами")
    else:
        sum_mutipl_vect = sum(list(map(lambda x, y: x * y, vect_1, vect_2)))
        sum_sq_root_vect_1 = sum([x ** 2 for x in vect_1]) ** 0.5
        sum_sq_root_vect_2 = sum([x ** 2 for x in vect_2]) ** 0.5
        res = sum_mutipl_vect / (sum_sq_root_vect_1 * sum_sq_root_vect_2)
        return res


print(cos_angle(a, b))