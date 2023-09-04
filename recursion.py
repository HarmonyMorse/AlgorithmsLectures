import time

# function which prints every nuber from N to zero
def print_numbers(n):
    for i in range(n, -1, -1):
        print(i)


# print_numbers(3)


# O(n) - the function gets called N times
def print_num(n):
    # a bse case (i.e. the code that tells us to stop running this function)
    print(n)
    if n == 0:
        return

    # recursive case (i.e. the case which takes us to the next sub-problem)
    print_num(n - 1)


# print_num(5)


# O(2^n)
def double_print_num(n):
    print(n)
    if n == 0:
        return

    double_print_num(n-1)
    double_print_num(n-1)
    return


double_print_num(3)