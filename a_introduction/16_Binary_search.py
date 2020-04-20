def binary_search(numbers, number_to_find, low, high):
    if low > high:
        return False

    numbers.sort()
    mid = (low + high)//2

    if numbers[mid] == number_to_find:
        return True

    elif numbers[mid] > number_to_find:
        return binary_search(numbers[low:mid], number_to_find, 0, mid - 1)
    else:
        return binary_search(numbers[mid + 1:], number_to_find, 0, mid)


def run():
    numbers = [5, 6, 3, 1, 67, 21, 44, 33, 12, 63, 46, 68, 11, 34, 99, 19]
    number_to_find = int(input("Input the number that you want to find: "))

    result = binary_search(numbers, number_to_find, 0, len(numbers) - 1)

    if result:
        print("The number has been found")
    else:
        print("The number hasn't been found")


if __name__ == "__main__":
    run()
