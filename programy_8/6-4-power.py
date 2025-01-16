numbers = list(range(1, 21))


def main():
    third_powers = list(map(lambda x: x ** 3, numbers))

    print("Original numbers and their third powers:")
    for num, power in zip(numbers, third_powers):
        print(f"{num} → {power}")


if __name__ == "__main__":
    main()