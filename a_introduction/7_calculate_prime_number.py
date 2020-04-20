def is_prime(number):
    if number < 2:

        return False
    elif number % 2 == 0:

        return False
    else:
        # Rango a partir de 3 hasta el número
        for i in range(3, number):
            if number % i == 0:

                return False

        return True


def run():
    number = int(input("Please, input a number: "))
    result = is_prime(number)
    if result:
        print("Your number is prime")
    else:
        print("Your number is no prime")


if __name__ == "__main__":
    run()
