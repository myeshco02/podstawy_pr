import statistics


class Statistics:
    def __init__(self, init_numbers=None):
        self.numbers = init_numbers

    def addNumber(self, num):
        try:
            self.numbers.append(num)
            print(f"Number {num} added successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def displayNumbers(self):
        print("Numbers:", " ".join(map(str, self.numbers)))

    def getMax(self):
        return max(self.numbers)

    def getMin(self):
        return min(self.numbers)

    def calcMean(self):
        return statistics.mean(self.numbers)

    def calcMedian(self):
        return statistics.median(self.numbers)

    def pStats(self):
        if not self.numbers:
            print("No numbers in the set.")
            return

        print("\nStatistical Quantities:")
        print(f"Minimum: {self.getMin()}")
        print(f"Maximum: {self.getMax()}")
        print(f"Arithmetic Mean: {self.calcMean()}")
        print(f"Median: {self.calcMedian()}")