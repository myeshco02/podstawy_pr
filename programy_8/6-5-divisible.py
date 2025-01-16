


def main():
    numbers = list(range(1, 21))

    divisible_numbers = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, numbers))

    print("Numbers divisible by 2 and 3:", divisible_numbers)
    

if __name__ == '__main__':
    main()
