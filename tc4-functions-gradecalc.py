############################################
# Tech Check 4 - Revised Version
# Customized entry of 6 different course grades and calculation of final grade point average.
############################################

# Student Name: Mathew Akunyili

def instructions():
    print("Grade Point Calculator\n")
    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0.\n")

def grade(course):
    return input(f"Please enter a letter grade for {course}: ").upper()

def modify():
    return input("Please enter a modifier (+, - or nothing): ")

def numeric(letterGrade, modifier):
    # Base numeric value for each grade
    numericGrade = {
        "A": 4.0,
        "B": 3.0,
        "C": 2.0,
        "D": 1.0,
        "F": 0.0
    }.get(letterGrade, -1)

    if numericGrade == -1:
        print("Invalid letter grade entered.")
        return None
    
    if modifier == "+":
        if letterGrade not in ("A", "F"):
            numericGrade += 0.3
    elif modifier == "-":
        if letterGrade != "F":
            numericGrade -= 0.3

    numericGrade = min(numericGrade, 4.0)
    
    return numericGrade

def output(course, numericGrade):
    print(f"The numeric value for {course} is: {numericGrade:.1f}")

def main():
    instructions()
    
    courses = ["PROG1700", "NET1700", "OSYS1200", "WEBD1000", "COMM1700", "DBAS1007"]
    total_grade_points = 0
    valid_courses = 0

    for course in courses:
        letterGrade = grade(course)
        modifier = modify()
        numericGrade = numeric(letterGrade, modifier)
        
        if numericGrade is not None:
            output(course, numericGrade)
            total_grade_points += numericGrade
            valid_courses += 1

    if valid_courses == 6:
        totalgrade = total_grade_points / valid_courses
        print(f"\nYour grade point average for the semester is: {totalgrade:.1f}")
    else:
        print("\nSome courses had invalid grades and were not counted towards Grade.")

main()
