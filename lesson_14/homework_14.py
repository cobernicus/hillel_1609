class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def change_average_grade(self, new_grade):
        self.average_grade = new_grade

    def display_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Average grade: {self.average_grade}")


student = Student("Edward", "Norton", 20, 3.8)
student.display_info()

student.change_average_grade(4.5)

print("\nAfter average grade changing:")
student.display_info()
