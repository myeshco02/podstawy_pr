# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.hair = ""

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student2.name = "Olivia"
    student2.age = 21

    student3 = Student()
    student3.name = "Kevin"
    student3.age = 20
    student3.hair = "black"

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old')
    print(f'{student2.name}, {student2.age} years old')
    print(f'{student3.name}, {student3.age} years old, and has {student3.hair} hair')


if __name__ == "__main__":
    main()