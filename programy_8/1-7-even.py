is_even = lambda number: number % 2 == 0


def main():
    test_numbers = [0, 1, 2, 3, 4, 5]

    for num in test_numbers:
        result = "even" if is_even(num) else "odd"
        print(f"{num} is {result}")


if __name__ == "__main__":
    main()
