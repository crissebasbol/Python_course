def foreign_exchange_calculator(amount):
    mex_to_col_rate = 145.97

    return mex_to_col_rate * amount


def run():
    print("Currency calculator")
    print("Convert Mexican pesos to Colombian\n")

    amount = float(input('Input the quantity of mexican pesos that you want to convert: '))

    result = foreign_exchange_calculator(amount)

    print("${} mexican pesos are ${} colombian pesos".format(amount, result))


if __name__ == "__main__":
    run()
