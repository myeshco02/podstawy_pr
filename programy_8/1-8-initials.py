initials = lambda name, surname: f"{name[0].upper()}.{surname[0].upper()}."


def main():
    test_cases = [
        ("John", "Doe"),
        ("alice", "smith"),
        ("robert", "JOHNSON"),
        ("mary ann", "van der waals")
    ]

    for name, surname in test_cases:
        init = initials(name, surname)
        print(f"{name} {surname}: {init}")


if __name__ == "__main__":
    main()
