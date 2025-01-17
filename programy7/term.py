import random


class Therm:
    def __init__(self):
        self.isOn = False
        self.currentTemp = None

    def turnOn(self):
        self.isOn = True
        print("Thermometer is turned on.")

    def turnOff(self):
        self.isOn = False
        self.currentTemp = None
        print("Thermometer is turned off.")

    def measureTemp(self):
        if not self.isOn:
            print("Thermometer is off. Cannot measure temperature.")
            return None

        self.currentTemp = round(random.uniform(34.0, 42.0), 1)
        return self.currentTemp

    def displayTemp(self):
        if not self.isOn:
            print("Thermometer is off. No temperature to display.")
            return

        if self.currentTemp is None:
            print("No temperature measurement yet.")
            return

        output = f"Temperature: {self.currentTemp}°C"

        if self.currentTemp >= 37.0:
            output += " (fever)"

        if self.currentTemp >= 41.0:
            output += " CRITICAL TEMPERATURE!!"

        print(output)