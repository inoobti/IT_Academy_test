from datetime import datetime


# Данные в формате дд/мм/гггг
date_1 = "05/06/2002"
date_2 = "24/07/2024"


def calc_data(d_1, d_2):
    first_date = datetime.strptime(d_1, "%d/%m/%Y")
    second_date = datetime.strptime(d_2, "%d/%m/%Y")
    result = abs((second_date - first_date).days)
    return result


print(calc_data(date_1, date_2))