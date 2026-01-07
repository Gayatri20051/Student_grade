import stud_grade

def test_average_calculation():
    expected_average = (85 + 78 + 92) / 3
    assert stud_grade.average == expected_average

def test_grade_assignment():
    # Average is 85 → Grade A
    assert stud_grade.grade == "A"

def test_student_name():
    assert stud_grade.name == "Gayatri"

def test_department():
    assert stud_grade.department == "Computer Science"
