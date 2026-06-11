# Shopping Cart Data
cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999]

# 1. Total cart value
total = sum(cart)
print("Total Cart Value: ₹", total)

# 2. Most expensive and cheapest product
most_expensive = max(cart)
cheapest = min(cart)

print("Most Expensive Product: ₹", most_expensive)
print("Cheapest Product: ₹", cheapest)

# 3. Premium shipping (price > 1000)
premium_count = 0
for price in cart:
    if price > 1000:
        premium_count += 1

print("Premium Shipping Eligible Products:", premium_count)

# 4. Discount list (price > 1500)
discount_list = []
for price in cart:
    if price > 1500:
        discount_list.append(price)

print("Discount Eligible Products:", discount_list)

# 5. Average price
average = total / len(cart)
print("Average Product Price: ₹", round(average, 1))