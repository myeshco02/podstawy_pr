import matplotlib.pyplot as plt

# Temperature data
data = {
    "Krakow": 7,
    "Warszawa": -2,
    "Sopot": 4,
    "Koszalin": -1,
    "Opole": 3
}


def main():
    # no idea what to use the map() for other than this:
    cities = list(map(str, data.keys()))
    temperatures = list(map(float, data.values()))

    plt.figure(figsize=(10, 6))
    plt.bar(cities, temperatures)



    plt.title('Temperature in Polish Cities')
    plt.xlabel('Cities')
    plt.ylabel('Temperature (°C)')

    plt.show()


if __name__ == '__main__':
    main()
