class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def __str__(self):
        nameIni = self.name[0]

        if self.age >= 18:
            return f"{self.surname.upper()}{nameIni.upper()}{self.seniority}"
        else:
            return f"{self.surname.lower()}{nameIni.lower()}{self.seniority}"


# Test cases
def main():
    # test 1: under 18
    t1 = C("Anna", "May", 17, 7)
    print(str(t1))

    # test 2: over 18
    t2 = C("George", "Brown", 21, 4)
    print(str(t2))


if __name__ == "__main__":
    main()
