def factorial(number):
    if number == 0:
        return 1

    return number * factorial(number - 1)


if __name__ == "__main__":
    number = int(input("Input a number: "))

    print(factorial(number))
