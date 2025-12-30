# Student Grading System

# Student details (hard-coded)
name = "Gayatri"
department = "Computer Science"
semester = "Semester 2"

# Marks (hard-coded)
m1 = 85
m2 = 78
m3 = 92

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
print("Average Marks:", round(average, 2))
print("Grade:", grade)
