class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km  # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print(f"Distance: {self.distance}\n")
        print(f"Rate: {self.rate_per_km}\n")
        print(f"Fare: {self.fare}")


def main():
    ride1 = TaxiRide(2.5)
    ride1.calculate_fare(10)
    ride1.print_receipt()
    print()

    ride2 = TaxiRide(4)
    ride2.calculate_fare(5)
    ride2.print_receipt()


if __name__ == "__main__":
    main()
