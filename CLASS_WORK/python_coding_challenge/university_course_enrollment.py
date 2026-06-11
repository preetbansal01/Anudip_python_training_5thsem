# Course Enrollment Data
enrollment = {
    "Python": 45,
    "Java": 38,
    "Data Science": 52,
    "Web Development": 34,
    "Machine Learning": 41,
    "Cloud Computing": 29,
    "Cyber Security": 33,
    "DBMS": 48,
    "Networking": 26,
    "Operating Systems": 37
}

# 1. Courses > 40 enrollments
def high_enrollment(data):
    print("Courses with More Than 40 Enrollments:", end=" ")
    for course, count in data.items():
        if count > 40:
            print(course, end=" ")
    print()

# 2. Most & least popular
def most_least(data):
    most = max(data, key=data.get)
    least = min(data, key=data.get)

    print("\nMost Popular Course:", most, f"({data[most]} students)")
    print("Least Popular Course:", least, f"({data[least]} students)")

# 3. Total enrollments
def total_enrollments(data):
    total = sum(data.values())
    print("\nTotal Enrollments:", total)

# 4. Categorization
def categorize(data):
    high = []
    medium = []
    low = []

    for course, count in data.items():
        if count > 40:
            high.append(course)
        elif 30 <= count <= 40:
            medium.append(course)
        else:
            low.append(course)

    print("\nHigh Demand:", high)
    print("Medium Demand:", medium)
    print("Low Demand:", low)

# 5. Promotion required (<35)
def promotion(data):
    count = 0
    for v in data.values():
        if v < 35:
            count += 1

    print("\nCourses Requiring Promotion:", count)


# ---------------- MAIN ----------------

high_enrollment(enrollment)
most_least(enrollment)
total_enrollments(enrollment)
categorize(enrollment)
promotion(enrollment)