# Attendance Management System

# Read file
def read_attendance(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                emp_id, status = line.split(",")
                data.append([emp_id, status])
    return data


# 1. Count present and absent
def count_attendance(data):
    present = 0
    absent = 0

    for emp in data:
        if emp[1] == "P":
            present += 1
        else:
            absent += 1

    print("Present Employees:", present)
    print("Absent Employees:", absent)

    return present, absent


# 2. Absent employee IDs
def show_absent(data):
    print("\nAbsent Employee IDs:", end=" ")
    for emp in data:
        if emp[1] == "A":
            print(emp[0], end=" ")
    print()


# 3. Attendance percentage
def attendance_percentage(present, total):
    percent = (present / total) * 100
    print(f"\nAttendance Percentage: {percent:.1f}%")


# 4. Generate absent report file
def generate_absent_report(data, filename):
    with open(filename, "w") as file:
        for emp in data:
            if emp[1] == "A":
                file.write(emp[0] + "\n")

    print("\nAbsentee Report Generated Successfully.")


# 5. Attendance award eligibility
def award_eligibility(data):
    all_present = True

    for emp in data:
        if emp[1] == "A":
            all_present = False
            break

    print("\nAttendance Award Eligibility:", end=" ")
    if all_present:
        print("Eligible")
    else:
        print("Not Applicable")


# ---------------- MAIN PROGRAM ----------------

data = read_attendance("attendance.txt")

present, absent = count_attendance(data)

show_absent(data)

attendance_percentage(present, len(data))

generate_absent_report(data, "absent_report.txt")

award_eligibility(data)