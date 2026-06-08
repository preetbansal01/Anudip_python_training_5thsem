performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# Display employees scoring above 80
print("Employees Scoring Above 80:")
for i in performance:
    if performance[i] > 80:
        print(i)

# Variables for top performer and average calculation
top_emp = ""
high = -1
total = 0
improvement = 0

# Lists for employee categories
excellent = []
good = []
average = []
poor = []

# Traverse dictionary
for i in performance:

    # Calculate total score
    total += performance[i]

    # Find top performer
    if performance[i] > high:
        high = performance[i]
        top_emp = i

    # Count employees needing improvement
    if performance[i] < 60:
        improvement += 1

    # Categorize employees
    if performance[i] >= 90:
        excellent.append(i)
    elif performance[i] >= 75:
        good.append(i)
    elif performance[i] >= 60:
        average.append(i)
    else:
        poor.append(i)

# Calculate average score
avg = total / len(performance)

# Display results
print("\nTop Performer:", top_emp, "(", high, ")")
print("Employees Needing Improvement:", improvement)
print("Average Score:", round(avg, 1))
print("Excellent:", excellent)
print("Good:", good)
print("Average:", average)
print("Poor:", poor)