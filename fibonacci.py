# Fibonacci Sequence - O(2^n)
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
import time


# fib(n) = fib(n-1) + fib(n-2)
# Base case:
# at n = 0, fib(0) == 0
# at n = 1, fib(1) == 1
def fib(n):
    # Base case
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive case:
    result = fib(n-1) + fib(n-2)
    return result


start_time = time.time()
print(fib(30))
end_time = time.time()
print(f"runtime: {end_time - start_time} seconds")


# Memoization = cache the result of your function calls -> O(n)
def mem_fib(n, cache):
    # Base case
    if n == 0:
        cache[0] = 0
        return 0
    if n == 1:
        cache[1] = 1
        return 1

    if n in cache:
        return cache[n]

    result_n_1 = mem_fib(n - 1, cache)
    result_n_2 = mem_fib(n - 2, cache)
    result_at_n = result_n_1 + result_n_2
    cache[n] = result_at_n
    # Recursive case:
    return result_at_n


start_time = time.time()
cache = {}
print(mem_fib(35, cache))
end_time = time.time()
print(f"runtime: {end_time - start_time} seconds")


# Tabulation = start from 0 and go UP to n -> O(n)
def tab_fib(n):
    # start at n=0 and n=1
    # [0, ..... 0] length <- n
    # [0, 1, 1 ,2, 3,..]
    solution_table = [0 for _ in range(0, n + 1)]
    solution_table[0] = 0
    solution_table[1] = 1

    for i in range(2, n + 1):
        solution_table[i] = solution_table[i - 1] + solution_table[i - 2]

    return solution_table[n]


start_time = time.time()
print(tab_fib(35))
end_time = time.time()
print(f"runtime: {end_time - start_time} seconds")
