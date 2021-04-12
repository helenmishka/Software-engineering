from homework import *

global NOT_CHANGED
NOT_CHANGED = -2

def change_array_should_return_error_for_array_without_prime_numbers():
    a = [84, 24, 26, 28]
    expected = NOT_CHANGED
    actuall = change_array(a)
    if(actuall != expected):
        print("change_array_should_return_error_for_array_without_prime_numbers FAILED\n"\
              "Expected result:",expected,"\nActuall result:",actuall) 
        return 1;
    else:
        print("change_array_should_return_error_for_array_without_prime_numbers OK")
        return 0
def change_array_should_return_array_for_array_with_prime_numbers():
    a = [1, 2, 11, 24, 56]
    expected = [1, 2, 2, 11, 2, 24, 56]
    actuall = change_array(a)
    if(actuall != expected):
        print("change_array_should_return_array_for_array_with_prime_numbers FAILED\n"\
              "Expected result:",expected,"\n Actuall result:",actuall) 
        return 1;
    else:
        print("change_array_should_return_array_for_array_with_prime_numbers OK")
        return 0
def change_array_should_return_array_for_array_with_one_prime_number():
    a = [11]
    expected = [11, 2]
    actuall = change_array(a)
    if(actuall != expected):
        print("change_array_should_return_array_for_array_with_one_prime_number FAILED\n"\
              "Expected result:",expected,"\n Actuall result:",actuall) 
        return 1;
    else:
        print("change_array_should_return_array_for_array_with_one_prime_number OK")
        return 0
def change_array_should_return_array_for_array_only_with_prime_numbers():
    a = [11, 19, 3]
    expected = [11, 2, 19, 10, 3, 3]
    actuall = change_array(a)
    if(actuall != expected):
        print("change_array_should_return_array_for_array_only_with_prime_numbers FAILED\n"\
              "Expected result:",expected,"\n Actuall result:",actuall) 
        return 1;
    else:
        print("change_array_should_return_array_for_array_only_with_prime_numbers OK")
        return 0
def change_array_should_return_array_for_array_where_prime_number_is_last():
    a = [24, 32, 45, 58, 17]
    expected = [24, 32, 45, 58, 17, 8]
    actuall = change_array(a)
    if(actuall != expected):
        print("change_array_should_return_array_for_array_where_prime_number_is_last FAILED\n"\
              "Expected result:",expected,"\n Actuall result:",actuall) 
        return 1;
    else:
        print("change_array_should_return_array_for_array_where_prime_number_is_last OK")
        return 0
def change_array_should_return_array_for_array_where_prime_number_is_first():
    a = [11, 28, 98]
    expected = [11, 2, 28, 98]
    actuall = change_array(a)
    if(actuall != expected):
        print("change_array_should_return_array_for_array_where_prime_number_is_first FAILED\n"\
              "Expected result:",expected,"\n Actuall result:",actuall) 
        return 1;
    else:
        print("change_array_should_return_array_for_array_where_prime_number_is_first OK")
        return 0
def change_array_test():
    count = change_array_should_return_error_for_array_without_prime_numbers() + \
            change_array_should_return_array_for_array_with_prime_numbers() + \
            change_array_should_return_array_for_array_with_one_prime_number() + \
            change_array_should_return_array_for_array_only_with_prime_numbers() + \
            change_array_should_return_array_for_array_where_prime_number_is_last() + \
            change_array_should_return_array_for_array_where_prime_number_is_first()
    print(count,"tests is FAILED")


def is_prime_should_return_true_if_number_is_prime():
    n = 5
    expected = True
    actuall = is_prime(n)
    if(actuall != expected):
        print("is_prime_should_return_true_if_number_is_prime FAILED\n"\
              "Expected result:",expected,"\n Actuall result:",actuall) 
        return 1;
    else:
        print("is_prime_should_return_true_if_number_is_prime OK")
        return 0
def is_prime_should_return_false_if_number_is_not_prime():
    n = 6
    expected = False
    actuall = is_prime(n)
    if(actuall != expected):
        print("is_prime_should_return_false_if_number_is_not_prime FAILED\n"\
              "Expected result:",expected,"\n Actuall result:",actuall) 
        return 1;
    else:
        print("is_prime_should_return_false_if_number_is_not_prime OK")
        return 0
def is_prime_should_return_false_if_number_is_one():
    n = 1
    expected = False
    actuall = is_prime(n)
    if(actuall != expected):
        print("is_prime_should_return_false_if_number_is_one FAILED\n"\
              "Expected result:",expected,"\n Actuall result:",actuall) 
        return 1;
    else:
        print("is_prime_should_return_false_if_number_is_one OK")
        return 0
def is_prime_should_return_false_if_number_is_negative():
    n = -5
    expected = False
    actuall = is_prime(n)
    if(actuall != expected):
        print("is_prime_should_return_false_if_number_is_negative FAILED\n"\
              "Expected result:",expected,"\n Actuall result:",actuall) 
        return 1;
    else:
        print("is_prime_should_return_false_if_number_is_negative OK")
        return 0

def is_prime_test():
    count = is_prime_should_return_true_if_number_is_prime() + \
            is_prime_should_return_false_if_number_is_not_prime() + \
            is_prime_should_return_false_if_number_is_one() + \
            is_prime_should_return_false_if_number_is_negative()
    print(count,"tests is FAILED")


def sum_digits_should_return_sum_if_number_more_nine():
    n = 15
    expected = 6
    actuall = sum_digits(n)
    if(actuall != expected):
        print("sum_digits_should_return_sum_if_number_more_nine FAILED\n"\
              "Expected result:",expected,"\n Actuall result:",actuall) 
        return 1;
    else:
        print("sum_digits_should_return_sum_if_number_more_nine OK")
        return 0
    
def sum_digits_should_return_digits_if_number_les_ten():
    n = 6
    expected = n
    actuall = sum_digits(n)
    if(actuall != expected):
        print("sum_digits_should_return_digits_if_number_les_ten FAILED\n"\
              "Expected result:",expected,"\n Actuall result:",actuall) 
        return 1;
    else:
        print("sum_digits_should_return_digits_if_number_les_ten OK")
        return 0

def sum_digits_test():
    count = sum_digits_should_return_digits_if_number_les_ten() + \
            sum_digits_should_return_sum_if_number_more_nine()
    print(count,"tests is FAILED")
    

def insert_sum_should_return_array_if_index_is_zero():
    a = [5, 2, 1, 4]
    ind = 0
    n = 8
    expected = [8, 5, 2, 1, 4]
    actuall = insert_sum(a, ind, n)
    if(actuall != expected):
        print("insert_sum_should_return_array_if_index_is_zero FAILED\n"\
              "Expected result:",expected,"\n Actuall result:",actuall) 
        return 1;
    else:
        print("insert_sum_should_return_array_if_index_is_zero OK")
        return 0
def insert_sum_should_return_array_if_index_is_len_array():
    a = [1, 2, 3, 4]
    ind = 4
    n = 5
    expected = [1, 2, 3, 4, 5]
    actuall = insert_sum(a, ind, n)
    if(actuall != expected):
        print("insert_sum_should_return_array_if_index_is_len_array FAILED\n"\
              "Expected result:",expected,"\n Actuall result:",actuall) 
        return 1;
    else:
        print("insert_sum_should_return_array_if_index_is_len_array OK")
        return 0

def insert_sum_should_return_array_if_any_other_index():
    a = [1, 2, 5]
    ind = 1
    n = 3
    expected = [1, 3, 2, 5]
    actuall = insert_sum(a, ind, n)
    if(actuall != expected):
        print("insert_sum_should_return_array_if_any_other_index FAILED\n"\
              "Expected result:",expected,"\n Actuall result:",actuall) 
        return 1;
    else:
        print("insert_sum_should_return_array_if_any_other_index OK")
        return 0
def insert_sum_test():
    count = insert_sum_should_return_array_if_index_is_zero() + \
            insert_sum_should_return_array_if_index_is_len_array() + \
            insert_sum_should_return_array_if_any_other_index()
    print(count,"tests is FAILED")

def main():
    change_array_test()
    print()
    is_prime_test()
    print()
    sum_digits_test()
    print()
    insert_sum_test()
if __name__ == "__main__":
    main()
