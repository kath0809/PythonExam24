import random


def random_numbers(n=10, min_val=1, max_val=50):
    return [random.randint(min_val, max_val) for _ in range(n)]


def substitute(lst):
    return [num**2 if num % 5 == 0 else num for num in lst]


def main():
    numbers = random_numbers()
    print(f"Before substitution, the list is: {numbers}")
    numbers = substitute(numbers)
    print(f"After substitution, the list is: {numbers}")


main()
