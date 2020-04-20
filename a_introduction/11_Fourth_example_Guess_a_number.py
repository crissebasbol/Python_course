import random


def run():
    number_found = False
    random_number = random.randint(0, 20)

    while not number_found:
        number = int(input("Input a number for guess: "))

        if number == random_number:
            print("Congratulations")
            number_found = True
        elif number > random_number:
            print("The number must be smaller")
        else:
            print("The number must be greater")


if __name__ == "__main__":
    run()
