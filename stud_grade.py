# stud_grade.py
import sys

def calculate_grade(m1, m2, m3):
    avg = (m1 + m2 + m3) / 3
    if 90 <= avg <= 100:
        grade = "S"
    elif 80 <= avg < 90:
        grade = "A"
    elif 65 <= avg < 80:
        grade = "B"
    elif 50 <= avg < 65:
        grade = "C"
    elif 40 <= avg < 50:
        grade = "D"
    else:
        grade = "Fail"
    return avg, grade

if __name__ == "__main__":
    # Expecting 6 arguments
    if len(sys.argv) != 7:
        print("Usage: python stud_grade.py <name> <department> <semester> <m1> <m2> <m3>")
        sys.exit(1)

    name = sys.argv[1]
    department = sys.argv[2]
    semester = sys.argv[3]
    m1 = float(sys.argv[4])
    m2 = float(sys.argv[5])
    m3 = float(sys.argv[6])

    avg, grade = calculate_grade(m1, m2, m3)

    print("\n---- Student Grading System ----")
    print("Name:", name)
    print("Department:", department)
    print("Semester:", semester)
    print("Marks:", m1, m2, m3)
    print("Average:", round(avg, 2))
    print("Grade:", grade)
