# Student Grading System

# Input student details
name = input("Enter student name: ")
department = input("Enter department: ")
semester = input("Enter semester: ")

# Input marks
m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))

# Calculate average
average = (m1 + m2 + m3) / 3

# Grade assignment
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
    grade = "F"

# Output
print("\n--- Student Report ---")
print("Name:", name)
print("Department:", department)
print("Semester:", semester)
print("Average Marks:", average)
print("Grade:", grade)
