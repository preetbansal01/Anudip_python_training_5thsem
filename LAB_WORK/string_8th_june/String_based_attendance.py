attendance = "PPAPPPAAPPPPAPP"

present = attendance.count('P')
absent = attendance.count('A')

total_days = len(attendance)
percentage = (present / total_days) * 100

# Longest Present Streak
max_present_streak = 0
current_present = 0

# Longest Absent Streak
max_absent_streak = 0
current_absent = 0

for day in attendance:
    if day == 'P':
        current_present += 1
        current_absent = 0
        max_present_streak = max(max_present_streak, current_present)
    else:
        current_absent += 1
        current_present = 0
        max_absent_streak = max(max_absent_streak, current_absent)

print("Attendance Record:", attendance)
print("\nPresent Days:", present)
print("\nAbsent Days:", absent)
print(f"\nAttendance Percentage: {percentage:.2f}%")
print("\nLongest Present Streak:", max_present_streak)
print("\nLongest Absent Streak:", max_absent_streak)

if percentage < 75:
    print("\nAttendance Status: Below 75%")
else:
    print("\nAttendance Status: 75% or Above")

print("\nComment: The student's attendance is slightly below the required 75%. Regular attendance is recommended.")