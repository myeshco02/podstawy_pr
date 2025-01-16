speeds = [48, 47, 54, 50, 42, 68, 39, 46]


def main():
    max_speed = 50

    print("Recorded values:", ",".join(map(str, speeds)))

    speeding_vehicles = list(filter(lambda speed: speed > max_speed, speeds))
    print("Speed too high:", ",".join(map(str, speeding_vehicles)))


if __name__ == "__main__":
    main()