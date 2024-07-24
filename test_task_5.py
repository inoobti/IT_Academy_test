def correct_word(count):
    if count == 1:
        return "слово"
    elif 1 < count < 5:
        return "слова"
    else:
        return "слов"


def check_amount_of_words(args):
    words_list = args
    amount_dict = {}
    length = len(words_list)
    for i in words_list:
        if i == "":
            words_count = 0
        else:
            words_count = len(str(i).split(" "))

        if str(words_count) in amount_dict.keys():
            amount_dict[str(words_count)] += 1
        else:
            amount_dict[str(words_count)] = 1

    amount_dict = dict(sorted(amount_dict.items()))
    result = ""
    for key, value in amount_dict.items():
        result += f"{key} {correct_word(int(key))}: {round(value * 100 / length)}%\n"
    return result


search_queries = ["watch new movies", "coffee near me", "how to find the determinant", "python",
                  "data science jobs in UK", "courses for data science", "taxi", "google", "yandex",
                  "bing","foreign exchange rates USD/BYN", "Netflix movies watch online free",
                  "Statistics courses online from top universities"]


print(check_amount_of_words(search_queries))

