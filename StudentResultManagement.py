students = [
    {"name" : "Asha", "marks" : [80, 75, 90]},
    {"name" : "Rafi", "marks" : [45, 50, 55]},
    {"name" : "Nila", "marks" : [92, 88, 95]},
    {"name" : "Rafik", "marks" : [100, 72, 85]}
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

    if student["name"] == "Nila":
        continue

    if average >= 50:
        passedStudents.append(student["name"])

    if average > highestAverage:
        highestAverage = average
        highestMarksStudent = student["name"]

    if average >= 80:
        topStudents.append(student["name"])

    print(f"Name: {student['name']} Average: {average:.2f}")

print(f"\nPassed Students : {passedStudents}")
print(f"Highest Scoring Students : {highestMarksStudent}")
print(f"Excellent Students : {topStudents}")
print(f"Unique Marks : {uniqueMarks}")
