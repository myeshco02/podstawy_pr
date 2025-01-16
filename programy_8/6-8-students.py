scores = [37, 51, 44, 23, 78, 92, 39, 84, 83, 51]


def min_pts(limit):
    return lambda pts: pts >= limit


def main():
    filtered_results = {}

    # thresholds to check
    thresholds = [70, 40, 30]

    for threshold in thresholds:
        filtered_scores = list(filter(min_pts(threshold), scores))

        filtered_results[threshold] = filtered_scores
        print(f"Min {threshold} pts: {filtered_scores}")


if __name__ == '__main__':
    main()
