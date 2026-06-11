# Student Marks Management System

# Read data from file
def read_students(filename):
    students = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                sid, name, marks = line.split(",")
                students.append([sid, name, int(marks)])
    return students


# 1. Count pass and fail students
def count_pass_fail(students):
    passed = 0
    failed = 0

    for s in students:
        if s[2] >= 40:
            passed += 1
        else:
            failed += 1

    print("Passed Students:", passed)
    print("Failed Students:", failed)


# 2. Display topper
def display_topper(students):
    topper = students[0]

    for s in students:
        if s[2] > topper[2]:
            topper = s

    print("\nTopper:", topper[1], f"({topper[2]})")


# 3. Merit certificate holders (>= 90)
def merit_students(students):
    print("\nMerit Certificate Holders:")
    for s in students:
        if s[2] >= 90:
            print(s[1], end=" ")
    print()


# 4. Generate report card file
def generate_report(students,  .txt):
    with open(filename, "w") as file:
        for s in students:
            sid, name, marks = s

            if marks >= 40:
                result = "Pass"
            else:
                result = "Fail"

            file.write(f"{sid},{name},{marks},{result}\n")

    print("\nReport Cards Generated Successfully.")


# ---------------- MAIN PROGRAM ----------------

students = read_students("marks.txt")

count_pass_fail(students)
display_topper(students)
merit_students(students)
generate_report(students, "report_card.txt")