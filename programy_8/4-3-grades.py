grades = [3.0, 5.0, 2.0, 3.5, 4.0, 4.0, 3.5, 2.0, 4.0, 2.0]


def main():
    filtered_grades = list(filter(lambda grade: grade != 2.0, grades))

    average = sum(filtered_grades) / len(filtered_grades)

    print("Original grades:", grades)
    print(f"Arithmetic mean for grades <> 2.0 is {average:.2f}")


if __name__ == "__main__":
    main()