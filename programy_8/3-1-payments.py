payments = [
    15.90,
    38.47,
    4.07,
    132.70,
    9.15
]


def main():
    for payment in map(lambda x: x * 4.5, payments):
        print(round(payment, 2))


if __name__ == '__main__':
    main()
