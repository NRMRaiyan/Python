students = [
    {"name" : "Aisha", "marks" : [90, 81, 97, 80]},
    {"name" : "Rafi", "marks" : [51, 75, 43, 59]},
    {"name" : "Nila", "marks" : [74, 67, 87, 81]}
]

passedStudents = []
highestMarksStudent = ""
highestAverage = 0
topStudents = []
uniqueMarks = set()

for student in students:

    for mark in student["marks"]:
        uniqueMarks.add(mark)

    total = sum(student["marks"])
    average = total / len(student["marks"])

    if average >= 50:
        passedStudents.append(student["name"])

    if average > highestAverage:
        highestAverage = average
        highestMarksStudent = student["name"]

    if student["name"] == "Nila":
        continue

    print(f"Name: {student['name']} Average: {average:.2f}")

