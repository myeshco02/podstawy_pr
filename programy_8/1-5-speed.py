def avg_speed(distance, hours, minutes):
    total_hours = hours + (minutes / 60)
    return distance / total_hours


def main():
    distance = float(input("Enter distance in km: "))
    hours = int(input("Enter number of travel hours: "))
    minutes = int(input("Enter number of travel minutes: "))

    speed = avg_speed(distance, hours, minutes)
    print(f"Average speed: {speed:.1f} km/h")


if __name__ == "__main__":
    main()