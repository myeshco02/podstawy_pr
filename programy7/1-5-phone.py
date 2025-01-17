class Smartphone:
    def __init__(self, brand, model, battery_level, is_on, is_locked):
        self.brand = brand
        self.model = model
        self.battery_level = battery_level  
        self.is_on = is_on  
        self.is_locked = is_locked  

    # Behaviors (Methods)
    def power_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now powered on.")
        else:
            print(f"{self.brand} {self.model} is already on.")

    def power_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now powered off.")
        else:
            print(f"{self.brand} {self.model} is already off.")

    def lock_screen(self):
        if self.is_on and not self.is_locked:
            self.is_locked = True
            print("The screen is locked.")
        elif not self.is_on:
            print("Cannot lock the screen because the phone is off.")
        else:
            print("The screen is already locked.")

    def unlock_screen(self):
        if self.is_on and self.is_locked:
            self.is_locked = False
            print("The screen is now unlocked.")
        elif not self.is_on:
            print("Cannot unlock the screen because the phone is off.")
        else:
            print("The screen is already unlocked.")

    def use_battery(self, percentage):
        if self.is_on:
            if self.battery_level - percentage >= 0:
                self.battery_level -= percentage
                print(f"Battery used: {percentage}%. Remaining battery: {self.battery_level}%.")
            else:
                self.battery_level = 0
                print("Battery fully drained. Please recharge.")
        else:
            print("Cannot use battery because the phone is off.")

    def charge_battery(self, percentage):
        if self.battery_level + percentage <= 100:
            self.battery_level += percentage
        else:
            self.battery_level = 100
        print(f"Battery charged to: {self.battery_level}%.")

# Create a smartphone object
my_phone = Smartphone(brand="Samsung", model="Galaxy S22", battery_level=50, is_on=False, is_locked=False)

# Call methods 
my_phone.power_on()
my_phone.unlock_screen()
my_phone.use_battery(20)
my_phone.lock_screen()
my_phone.charge_battery(40)
my_phone.power_off()

# Display object's properties
print("\nSmartphone Properties:")
print(f"Brand: {my_phone.brand}")
print(f"Model: {my_phone.model}")
print(f"Battery Level: {my_phone.battery_level}%")
print(f"Is On: {my_phone.is_on}")
print(f"Is Locked: {my_phone.is_locked}")