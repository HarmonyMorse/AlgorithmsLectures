
# Constant time O(1)
def print_num(n):
    print(n)


# Constant time O(1000)
def print_num_1000(n):
    for _ in range(1000):
        print(n)


# Linear time O(n)
def print_num_n_times(n):
    for _ in range(n):
        print(n)


# Linear time O(n)
def print_num_n_times(n):
    for _ in range(n):  # O(n) * O(1) * O(1000) = O(n)
        print(n)  # O(1)
        for _ in range(1000):  # O(1000)
            print(n)


# Polynomial time O(n^2) -- in this case, it's specifically quadratic
animals = ['duck', 'jackal', 'hippo', 'aardvark', 'cat', 'flamingo', 'iguana', 'giraffe', 'elephant', 'bear']


def print_animal_pairs():
    for animal_1 in animals:  # O(n) * O(n) = O(n^2)
        for animal_2 in animals:  # O(n)
            print(f'{animal_1} and {animal_2}')  # O(1)


# Logarithmic time O(log(n))
# we are removing half of the remaining animals each time
# the input gets reduced by a factor each iteration
def free_animals(animals_list):
    while len(animals_list) > 0:
        animals_list = animals_list[0: len(animals_list // 2)]