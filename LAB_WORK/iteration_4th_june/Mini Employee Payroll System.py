# Employee Salary Calculator

name = input("Enter Employee Name: ")
basic_salary = float(input("Enter Basic Salary: ₹"))

# Calculations
hra = basic_salary * 0.20 
da = basic_salary * 0.10
pf = basic_salary * 0.12

gross_salary = basic_salary + hra + da
net_salary = gross_salary - pf

# Grade Determination
if net_salary > 50000:
    grade = "Senior Grade"
elif net_salary > 30000:
    grade = "Mid Grade"
else:
    grade = "Junior Grade"

# Display Results
print("\n----- Salary Details -----")
print("Employee Name :", name)
print("Basic Salary  : ₹", basic_salary)
print("HRA (20%)     : ₹", hra)
print("DA (10%)      : ₹", da)
print("PF (12%)      : ₹", pf)
print("Gross Salary  : ₹", gross_salary)
print("Net Salary    : ₹", net_salary)
print("Grade         :", grade)
