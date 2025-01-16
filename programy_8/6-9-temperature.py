temperatures = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}


def get_positive_temp_cities(temp_dict):
    positive_cities = list(filter(lambda city: temp_dict[city] > 0, temp_dict))
    return positive_cities


def main():
    positive_temp_cities = get_positive_temp_cities(temperatures)
    print("Cities with positive temperatures:", " ".join(positive_temp_cities))


if __name__ == '__main__':
    main()
