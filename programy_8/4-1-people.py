employees = ["SMITH Lucy", "JONES Janet", "LEE Jerry",
             "JACKSON Peter", "JOHNSON Rick",
             "LEWIS Terry", "CLARKE Robin"]


def main():
    emp_J = list(filter(lambda e: e[0] == "J", employees))
    for e in emp_J:
        print(e)


if __name__ == '__main__':
    main()
