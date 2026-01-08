import pytest
from student_grading import calculate_grade

# -------- Grade S (90–100) --------
def test_grade_s_1():
    avg, grade = calculate_grade(95, 92, 93)
    assert grade == "S"

def test_grade_s_2():
    avg, grade = calculate_grade(90, 90, 90)
    assert grade == "S"


# -------- Grade A (80–89) --------
def test_grade_a_1():
    avg, grade = calculate_grade(85, 82, 83)
    assert grade == "A"

def test_grade_a_2():
    avg, grade = calculate_grade(89, 88, 87)
    assert grade == "A"


# -------- Grade B (65–79) --------
def test_grade_b_1():
    avg, grade = calculate_grade(70, 72, 74)
    assert grade == "B"

def test_grade_b_2():
    avg, grade = calculate_grade(65, 66, 67)
    assert grade == "B"

def test_grade_b_3():
    avg, grade = calculate_grade(79, 78, 77)
    assert grade == "B"


# -------- Grade C (50–64) --------
def test_grade_c_1():
    avg, grade = calculate_grade(55, 58, 57)
    assert grade == "C"

def test_grade_c_2():
    avg, grade = calculate_grade(60, 62, 61)
    assert grade == "C"

def test_grade_c_3():
    avg, grade = calculate_grade(50, 52, 53)
    assert grade == "C"


# -------- Grade D (40–49) --------
def test_grade_d_1():
    avg, grade = calculate_grade(45, 42, 44)
    assert grade == "D"

def test_grade_d_2():
    avg, grade = calculate_grade(40, 41, 42)
    assert grade == "D"

def test_grade_d_3():
    avg, grade = calculate_grade(49, 48, 47)
    assert grade == "D"


# -------- Fail (<40) --------
def test_fail_1():
    avg, grade = calculate_grade(30, 35, 38)
    assert grade == "Fail"

def test_fail_2():
    avg, grade = calculate_grade(20, 25, 30)
    assert grade == "Fail"

def test_fail_3():
    avg, grade = calculate_grade(39, 38, 37)
    assert grade == "Fail"
