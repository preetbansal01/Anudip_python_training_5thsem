# Stock quantities
stock = [25, 5, 0, 12, 3, 18, 0, 30]

#Empty Lists for different categories
restock = []
healthy_stock = []

# Counters
out_of_stock = 0
available_products = 0

# Check each product quantity
for product in stock:

    # Count out-of-stock products
    if product == 0:
        out_of_stock += 1

    # Add products with stock less than 10
    if product < 10:
        restock.append(product)

    # Count available products
    if product > 0:
        available_products += 1

    # Add products with stock >= 15
    if product >= 15:
        healthy_stock.append(product)

# Display results
print("Out of Stock Products:", out_of_stock)
print("Restock Required:", restock)
print("Available Products:", available_products)
print("Healthy Stock:", healthy_stock)