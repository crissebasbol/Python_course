def first_not_repeating_chat(text):
    tuple_text = tuple(text)
    for character in tuple_text:
        count = tuple_text.count(character)
        if count == 1:
            return character
    return "_"


def run():
    text = str(input("Input a characters' sequence: "))
    result = first_not_repeating_chat(text)

    if result == "_":
        print("All characters repeat them")
    else:
        print("The first character no repeated is: {}".format(result))


if __name__ == "__main__":
    run()
