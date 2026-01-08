# student_grading.py
# Program to calculate student grade based on average marks

import sys

def calculate_grade(m1, m2, m3):
    """Calculate average and assign grade"""
    average = (m1 + m2 + m3) / 3

    if 90 <= average <= 100:
        grade = "S"
    elif 80 <= average < 90:
        grade = "A"
    elif 65 <= average < 80:
        grade = "B"
    elif 50 <= average < 65:
        grade = "C"
    elif 40 <= average < 50:
        grade = "D"
    else:
        grade = "Fail"

    return average, grade


if __name__ == "__main__":
    print("\n---- Student Grading System ----\n")

    try:
        # Case 1: Arguments passed (for Jenkins or CLI)
        # Expected order:
        # name department semester mark1 mark2 mark3
        if len(sys.argv) == 7:
            name = sys.argv[1]
            department = sys.argv[2]
            semester = sys.argv[3]
            m1 = float(sys.argv[4])
            m2 = float(sys.argv[5])
            m3 = float(sys.argv[6])

        # Case 2: No arguments passed (for console input)
        else:
            name = input("Enter student name: ")
            department = input("Enter department: ")
            semester = input("Enter semester: ")
            m1 = float(input("Enter marks in subject 1: "))
            m2 = float(input("Enter marks in subject 2: "))
            m3 = float(input("Enter marks in subject 3: "))

        # Display parameters
        print("\n=== Student Details ===")
        print("Name:", name)
        print("Department:", department)
        print("Semester:", semester)
        print("Marks:", m1, m2, m3)

        # Calculate result
        average, grade = calculate_grade(m1, m2, m3)

        print("\nAverage Marks:", f"{average:.2f}")
        print("Grade:", grade)

    except ValueError:
        print("Invalid input! Please enter numeric values for marks.")
