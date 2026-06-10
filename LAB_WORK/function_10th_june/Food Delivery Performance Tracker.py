delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# 1. Returns the shortest delivery time
def fastest_delivery(times):
    return min(times)

# 2. Returns a list of orders taking more than 45 minutes
def delayed_orders(times):
    return [time for time in times if time > 45]

# 3. Returns the average delivery time
def average_delivery_time(times):
    return sum(times) / len(times)

# 4. Displays order categories
def delivery_category(times):
    for time in times:
        if time <= 30:
            print(f"{time} -> Fast")
        elif time <= 45:
            print(f"{time} -> Normal")
        else:
            print(f"{time} -> Delayed")


# Driver Code
print("Fastest Delivery:", fastest_delivery(delivery_time), "minutes")

print("\nDelayed Orders:", delayed_orders(delivery_time))

print("\nAverage Delivery Time:",
      round(average_delivery_time(delivery_time), 1), "minutes")

print("\nCategories:")
delivery_category(delivery_time)