global EMPTY_STRING
EMPTY_STRING = -1
global ERROR
ERROR = -2


def sum_len_words(words):
    """
    @brief Функция подсчета суммы длин всех слов в строке
    @detailed Функция обрабатывает массив слов, находит длину каждого слова и далее находит сумму длин
    @param words массив слов
    @return sum_len сумма длин всех слов
    """
    sum_len = 0
    if len(words) == 0:
        return EMPTY_STRING
    for i in range(len(words)):
        len_words = 0
        for j in range(len(words[i])):
            len_words += 1
        sum_len += len_words
    return sum_len
def count_words(words):
    """
    @brief Функция подсчета количетсва слов в массиве 
    @detailed Функция обрабатывает массив слов, находит длину массива
    @param words массив слов
    @return count количество слов
    """
    count = 0
    if len(words) == 0:
        return EMPTY_STRING
    for i in range(len(words)):
        count += 1
    return count

def average(sum_len, count):
    """
    @brief Функция находит среднюю длину слова
    @param sum_len сумма длин
    @param count количетсво слов
    @return sred среднее значение длины
    """
    if (sum_len == EMPTY_STRING or count == EMPTY_STRING):
        return ERROR
    sred = sum_len / count
    return sred

def sum_len_words_should_return_sum_len_if_str_not_empty():
    words = ["lena","mama","papa","reka"]
    expected = 16
    actual = sum_len_words(words)
    if (actual != expected):
        print("sum_len_words_should_return_sum_len_if_str_not_empty FAILED")
        return 1
    else:
        print("sum_len_words_should_return_sum_len_if_str_not_empty OK")
        return 0
def sum_len_words_should_return_ERROR_if_str_empty():
    words = []
    expected = EMPTY_STRING
    actual = sum_len_words(words)
    if (actual != expected):
        print("sum_len_words_should_return_ERROR_if_str_empty FAILED")
        return 1
    else:
        print("sum_len_words_should_return_ERROR_if_str_empty OK")
        return 0

def count_words_should_return_ERROR_if_str_empty():
    words = []
    expected = EMPTY_STRING
    actual = count_words(words)
    if (actual != expected):
        print("count_words_should_return_ERROR_if_str_empty FAILED")
        return 1
    else:
        print("count_words_should_return_ERROR_if_str_empty OK")
        return 0
def count_words_should_return_count_if_str_not_empty():
    words = ["lena","mama","papa","reka"]
    expected = 4
    actual = count_words(words)
    if (actual != expected):
        print("count_words_should_return_count_if_str_not_empty FAILED")
        return 1
    else:
        print("count_words_should_return_count_if_str_not_empty OK")
        return 0

def average_should_return_ERROR_if_str_empty():
    sum_l = EMPTY_STRING
    count = EMPTY_STRING
    expected = ERROR
    actual = average(sum_l, count)
    if (actual != expected):
        print("average_should_return_ERROR_if_str_empty FAILED")
        return 1
    else:
        print("average_should_return_ERROR_if_str_empty OK")
        return 0
def average_should_return_result_if_str_not_empty():
    sum_l = 25
    count = 5
    expected = 5
    actual = average(sum_l, count)
    if (actual != expected):
        print("average_should_return_result_if_str_not_empty FAILED")
        return 1
    else:
        print("average_should_return_result_if_str_not_empty OK")
        return 0
        
if __name__ == "__main__":
    count = sum_len_words_should_return_sum_len_if_str_not_empty() + \
            sum_len_words_should_return_ERROR_if_str_empty() + \
            count_words_should_return_ERROR_if_str_empty() + \
            count_words_should_return_count_if_str_not_empty() + \
            average_should_return_ERROR_if_str_empty() + \
            average_should_return_result_if_str_not_empty()
            
    print(count, "FAILED")
            
            
