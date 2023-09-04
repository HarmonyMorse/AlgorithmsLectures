import random
import time

my_range = 100
my_size = 50

nums = list(range(0, my_size))

shuffled_nums = list(range(0, my_size))
random.shuffle(shuffled_nums)

random_nums = random.sample(range(my_range), my_size)


def partition(numbers):
    # this function breaks numbers into a left, pivot, and right
    left = []
    pivot = numbers[0]
    right = []

    # partition the numbers correctly into left and right arrays
    for num in numbers[1:]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)

    return left, pivot, right


def quicksort(numbers):
    # base case
    # what is the easiest array to sort
    if len(numbers) <= 1:
        return numbers

    # divide
    # figure out how to properly split the data
    left, pivot, right = partition(numbers)
    # make an array of size 1 with the pivot, this is now sorted
    pivot = [pivot]

    sorted_array = quicksort(left) + pivot + quicksort(right)

    return sorted_array


start_time = time.time()
# print(quicksort([5, 9, 3, 7, 2, 8, 1, 6, 4]))
print(quicksort(random_nums))
end_time = time.time()
print(f"runtime: {end_time - start_time} seconds")

# this is O(nlog(n)) runtime
