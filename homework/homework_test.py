global INPUT_ERROR
INPUT_ERROR = -1

global NOT_CHANGED
NOT_CHANGED = -2

def isint(s):
    try:
        int(s) 
        return True
    except ValueError:
        return False
    
def read_array():
    N = 400
    n = input()
    if not isint(n):
        print("ERROR")
        return INPUT_ERROR;
    n = int(n)
    if n <= 0:
        print("ERROR")
        return INPUT_ERROR;
    if n > N:
        print("ERROR")
        return INPUT_ERROR;
    a = [0]*n
    for i in range(n):
        a[i] = input()
    for i in range(n):
        if not isint(a[i]):
            print("ERROR")
            return INPUT_ERROR;
    for i in range(n):
        a[i] = int(a[i])
    return a

def print_array(a):
    for i in range(len(a)):
        print(a[i], end = ' ')

def is_prime(n):
    if n < 0:
        return False
    if n == 1:
        return False
    else:
        for i in range(2,n,1):
            if n % i == 0:
                return False
    return True

def sum_digits(n):
    summa = 0
    if n < 10:
        return n
    while n > 0:
        summa += int(n % 10)
        n = int(n / 10)
    return summa

def insert_sum(a, ind, n):
    a.append(1)
    for i in range(len(a) - 1, ind - 1, -1):
        a[i] = a[i-1]
    a[ind] = n
    return a

def change_array(a):
    i = 0
    len_a = len(a)
    while (i < len(a)):
        if is_prime(a[i]):
            summa = sum_digits(a[i])
            insert_sum(a, i+1, summa)
            i += 1
        i += 1
    len_change_a = len(a)
    if (len_a == len_change_a):
        print("ERROR")
        return NOT_CHANGED
    else:
        return a

def main():
    a = read_array()
    if (a != INPUT_ERROR):
        a = change_array(a)
        if (a != NOT_CHANGED):
            print_array(a)
if __name__ == "__main__":
    main()
