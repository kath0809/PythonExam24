def retrieve_numbers():
    while True:
        try:
            number = input("Enter an integer (blank to quit): ")
            if number == "":
                return None
            return int(number)
        except ValueError:
            print("Letters and symbols are not valid, try entering an integer.")
# It's useful to have a try-except block for when the input might not be an integer.


def append_number(number, positive_numbers, zeros, negative_numbers):
    if number > 0:
        positive_numbers.append(number)
    elif number == 0:
        zeros.append(number)
    else:
        negative_numbers.append(number)


def get_numbers():
    positive_numbers = []
    zeros = []
    negative_numbers = []

    while True:
        number = retrieve_numbers()
        if number is None:
            break
        append_number(number, positive_numbers, zeros, negative_numbers)

    return positive_numbers, zeros, negative_numbers


def merge_numbers(positive_numbers, zeros, negative_numbers):
    result = positive_numbers + zeros + negative_numbers
    print(f"The numbers were: {result}")


def categorize_and_merge():
    positive_numbers, zeros, negative_numbers = get_numbers()
    merge_numbers(positive_numbers, zeros, negative_numbers)


categorize_and_merge()
