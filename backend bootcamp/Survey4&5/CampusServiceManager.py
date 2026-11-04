#(A) Student Results
class Student:
    def __init__(self, name, student_id, marks):
        # Validate marks before storing the student data
        if not isinstance(marks, (int, float)) or isinstance(marks, bool):
            raise ValueError("Marks must be numeric")

        if not 0 <= marks <= 100:
            raise ValueError("Marks must be between 0 and 100")

        self.name = name
        self.student_id = student_id
        self.marks = marks

    def get_grade(self):
        if self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 50:
            return "D"
        else:
            return "F"

    def __str__(self):
        return (
            f"Name: {self.name}, "
            f"ID: {self.student_id}, "
            f"Marks: {self.marks}, "
            f"Grade: {self.get_grade()}"
        )


# Testing the Student class
student1 = Student("Rafi", "101", 85)
student2 = Student("Nila", "102", 47)

print(student1)
print(student2)
