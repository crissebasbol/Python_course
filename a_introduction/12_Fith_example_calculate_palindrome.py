def palindrome_method1(word):
    reversed_word = word[::-1]
    if reversed_word == word:
        return True
    else:
        return False


def palindrome_method2(word):
    reversed_letters = []

    for letter in word:
        reversed_letters.insert(0, letter)

    reversed_word = "".join(reversed_letters)

    if reversed_word == word:
        return True
    else:
        return False


def run():
    word = str(input("Input a word: "))

    if palindrome_method1(word):
        print("The word is palindrome")
    else:
        print("The word is not palindrome")

    if palindrome_method2(word):
        print("The word is palindrome")
    else:
        print("The word is not palindrome")


if __name__ == "__main__":
    run()
