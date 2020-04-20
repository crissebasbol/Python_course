def create_file():
    with open("numbers.txt", "w") as file:
        for i in range(10):
            file.write(str(i))


def read_file():
    # Enconding just to manage special characters, if the file doesn't have any special character,
    # this parameter is not necessary
    # When python read a file, all the lines break are saved in the next position of the list (file is a list)
    with open("aleph.txt", encoding="utf8") as file:
        print(file.readlines())


def find_in_file(word):
    counter = 0
    with open("aleph.txt", encoding="utf8") as file:
        for line in file:
            counter += line.count(word)

    print("{} was {} found in the file".format(word, counter))


def run():
    create_file()
    read_file()
    find_in_file("Beatriz")


if __name__ == "__main__":
    run()
