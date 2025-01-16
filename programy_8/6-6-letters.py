def main():
    employees = [
        ("Smith", "Lucy"),
        ("Jones", "Janet"),
        ("Lee", "Jerry"),
        ("Jackson", "Peter"),
        ("Johnson", "Rick"),
        ("Lewis", "Terry"),
        ("Clarke", "Robin")
    ]

    formatted_names = list(map(lambda emp: f"{emp[0].upper()}, {emp[1]}", employees))

    for name in formatted_names:
        print(name)


if __name__ == '__main__':
    main()
