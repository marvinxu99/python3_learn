# Use lambdas as in-place functions


def CelsisusToFahrenheit(temp):
    return (temp * 9/5) + 32


def FahrenheitToCelsisus(temp):
    return (temp-32) * 5/9


def main():
    ctemps = [0, 12, 34, 100, 37]
    ftemps = [32, 65, 100, 212, 101.3]

    # TODO: Use regular functions to convert temps
    print(list(map(CelsisusToFahrenheit, ctemps)))
    print(list(map(FahrenheitToCelsisus, ftemps)))

    # TODO: Use lambdas to accomplish the same thing
    print(list(map(lambda t: (t * 9/5) + 32, ctemps)))
    print(list(map(lambda t: (t - 32) * 5/9, ftemps)))


if __name__ == "__main__":
    main()
