num = int(input("Enter a number: "))

digits = len(str(num)) 
total = sum(int(digit) ** digits for digit in str(num))

if total == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
