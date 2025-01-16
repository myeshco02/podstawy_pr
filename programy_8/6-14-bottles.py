CAPACITY = 500
TOLERANCE = 0.02

measurements = [508, 500, 512, 499, 492, 511, 503, 476, 501, 509]


def main():
    lower_limit = CAPACITY * (1 - TOLERANCE)
    upper_limit = CAPACITY * (1 + TOLERANCE)

    incorrect_bottles = list(filter(lambda x: x < lower_limit or x > upper_limit, measurements))
    incorrect_percentage = (len(incorrect_bottles) / len(measurements)) * 100

    # Format output
    print(f"Bottle capacity:    {CAPACITY}ml")
    print(f"Filling tolerance:  {TOLERANCE * 100}%")
    print(f"Filled bottles:     {','.join(map(str, measurements))}")
    print(f"Incorrectly filled: {incorrect_percentage:.0f}%")


if __name__ == '__main__':
    main()
