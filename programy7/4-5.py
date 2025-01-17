from term import Therm


def main():
    thermometer = Therm()

    thermometer.turnOn()

    thermometer.measureTemp()

    thermometer.displayTemp()

    thermometer.turnOff()


if __name__ == "__main__":
    main()
