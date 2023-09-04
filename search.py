import random
import time

my_range = 100
my_size = 50

nums = list(range(0, my_size))

shuffled_nums = list(range(0, my_size))
random.shuffle(shuffled_nums)

random_nums = random.sample(range(my_range), my_size)

print(nums)
print(shuffled_nums)
print(random_nums)

num_to_find = 12


# O(n) - linear time
def linear_search(arr, target):
    for num in arr:
        if num == target:
            return True
    return False


print(linear_search(nums, num_to_find))
print(linear_search(shuffled_nums, num_to_find))
print(linear_search(random_nums, num_to_find))


random_nums.sort()
print(random_nums)


def binary_search(arr, target):
    start = 0
    end = (len(arr) - 1)
    found = False
    while end >= start and not found:
        middle_index = (start + end) // 2
        if arr[middle_index] == target:
            found = True
        else:
            if target < arr[middle_index]:
                end = middle_index - 1
            if target > arr[middle_index]:
                start = middle_index + 1
    return found


start_time = time.time()
print(binary_search(random_nums, num_to_find))
end_time = time.time()
print(f"runtime: {end_time - start_time} seconds")
