from functools import reduce

numbers = [2, 4, 6, 3, 7, 5]


def main():
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    total = reduce(lambda x, y: x + y, even_numbers)
    print(total)


if __name__ == '__main__':
    main()
