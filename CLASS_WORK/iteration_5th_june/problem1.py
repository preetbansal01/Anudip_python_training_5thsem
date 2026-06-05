# Marks list
marks = [78, 45, 92, 35, 88, 40, 99, 56, 25]

# Failed student count
count = 0

# Passed marks
new_marks = []

# Marks above 75
new_list = []

# Check each mark
for mark in marks:

    # Add passed marks
    if mark >= 40:
        new_marks.append(mark)

    # Add marks above 75
    if mark > 75:
        new_list.append(mark)

    # Count failed students
    if mark < 40:
        count += 1

print("Number of failed students:", count)

# Initialize max and min
max_mark = marks[0]
min_mark = marks[0]

# Find max and min marks
for mark in marks:
    if mark > max_mark:
        max_mark = mark

    if mark < min_mark:
        min_mark = mark

print("Maximum mark:", max_mark)
print("Minimum mark:", min_mark)

# Display results
print("Passed marks:", new_marks)
print("Marks above 75:", new_list)