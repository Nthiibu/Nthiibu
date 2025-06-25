gpa = float(input("Enter the student's high school GPA: "))
test_score = int(input("Enter the student's admission test score (0-100): "))

if (gpa >= 3.0 and test_score >= 60) or (gpa < 3.0 and test_score >= 80):
    print("Accept")
else:
    print("Reject")
