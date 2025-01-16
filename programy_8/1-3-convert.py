def ms_to_kmh(x):
    return x * 3.6


def main():
    test_speeds = [10, 35]

    for speed in test_speeds:
        converted_speed = ms_to_kmh(speed)
        print(f"{speed} m/s = {converted_speed} km/h")


if __name__ == '__main__':
    main()
