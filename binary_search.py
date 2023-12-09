from random import randint
def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = []

for number in range(1, 5_000_001):
    my_list.append(number)

random_number = randint(1, 5_000_001)

num = binary_search(my_list, random_number + 1)

if __name__ == '__main__':
    print(f"Number is True: {random_number}")
    print(f"Number: {num}")
