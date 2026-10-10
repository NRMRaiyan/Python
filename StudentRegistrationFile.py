def validate_cgpa(cgpa):
    if cgpa < 0.0 or cgpa > 4.0:
        raise ValueError("CGPA must be between 0.0 and 4.0.")
    return cgpa

def create_student(name, student_id, cgpa, department="CSE"):
    student_dict = {
        "name": name,
        "id": student_id,
        "cgpa": cgpa,
        "department": department
    }
    return student_dict

def calculate_percentage(cgpa):
    return (cgpa / 4.0) * 100

def display_student(student_dict, percentage):
    print(f"\nName: {student_dict['name']}")
    print(f"ID: {student_dict['id']}")
    print(f"Department: {student_dict['department']}")
    print(f"CGPA: {student_dict['cgpa']:.2f}")
    print(f"Percentage: {percentage:.2f}%")

def main():
    
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    department = "CSE"
    
    cgpa = None
    is_valid = False

    try:
        cgpa_input = input("Enter CGPA (0.0 to 4.0): ")
        cgpa = float(cgpa_input)
        validate_cgpa(cgpa)
    except ValueError as error:
        print(f"Invalid input: {error}")
    else:
        print("Success: CGPA input is valid!")
        is_valid = True
    finally:
        print("Validation completed!")

    if is_valid:
        student_info = create_student(name, student_id, cgpa, department)
        
        percentage = calculate_percentage(student_info["cgpa"])
        
        display_student(student_info, percentage)

main()