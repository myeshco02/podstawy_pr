test_results = [
    {"name": "Peter", "result": 27},
    {"name": "Anna", "result": 63},
    {"name": "Robert", "result": 92},
    {"name": "Paul", "result": 46},
    {"name": "Barbara", "result": 52}
]


def filter_students_by_score(students, min_score, max_score):
    filtered_students = list(filter(
        lambda student: min_score <= student['result'] <= max_score,
        students
    ))
    return filtered_students


def main():
    filtered_results = filter_students_by_score(test_results, 50, 70)

    print("Students with scores between 50 and 70 points:")
    for student in filtered_results:
        print(f"{student['name']}: {student['result']} points")


if __name__ == '__main__':
    main()
