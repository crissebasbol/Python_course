countries = {
    "mexico": 122,
    "colombia": 49,
    "argentina": 43,
    "chile": 18,
    "peru": 31
}


def run():
    while True:
        country = str(input("Input a country name: ")).lower()

        try:
            print("The population of {} is: {} millions".format(country, countries[country]))
        except KeyError:
            print("The population data of {} isn't available ".format(country))
            break


class PositionError(Exception):
    """Error in that position"""


if __name__ == "__main__":
    run()
    x = [1, 2]
    position = int(input("Input a position por get the value of the list: "))
    if position != 0 and position != 1:
        raise PositionError("Error, size list exceeded")
    else:
        print(x[position])
