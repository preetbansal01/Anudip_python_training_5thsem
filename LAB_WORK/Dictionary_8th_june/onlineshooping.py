sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

# Display products sold more than 20 times
print("Products Sold More Than 20 Times:")
for i in sales:
    if sales[i] > 20:
        print(i)

# Variables for best-selling and least-selling products
best = ""
least = ""
high = -1
low = 999

# Variables for total sales, promotion list, and count
total = 0
promo = []
count = 0

# Traverse dictionary
for i in sales:

    # Calculate total units sold
    total += sales[i]

    # Find best-selling product
    if sales[i] > high:
        high = sales[i]
        best = i

    # Find least-selling product
    if sales[i] < low:
        low = sales[i]
        least = i

    # Add products with sales less than 15 to promotion list
    if sales[i] < 15:
        promo.append(i)

    # Count products having sales between 10 and 30
    if 10 <= sales[i] <= 30:
        count += 1

# Display results
print("\nBest Selling Product:", best, "(", high, ")")
print("Least Selling Product:", least, "(", low, ")")
print("Total Units Sold:", total)
print("Products Requiring Promotion:", promo)
print("Products Having Sales Between 10 and 30:", count)