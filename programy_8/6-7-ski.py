scores = [
    (17, 15, 16, 17, 15),
    (16, 18, 19, 17, 19),
    (19, 15, 15, 19, 18),
    (18, 17, 19, 15, 16)
]


def calculate_score(jumper_scores):
    total_sum = sum(jumper_scores)
    lowest_score = min(jumper_scores)
    highest_score = max(jumper_scores)

    return total_sum - lowest_score - highest_score


def main():
    total_points = list(map(calculate_score, scores))

    print(total_points)

    for i, (score, jumper_scores) in enumerate(zip(total_points, scores), 1):
        print(f"Competitor {i}:")
        print(f"  Scores: {jumper_scores}")
        print(f"  Total points: {score}")


if __name__ == '__main__':
    main()
