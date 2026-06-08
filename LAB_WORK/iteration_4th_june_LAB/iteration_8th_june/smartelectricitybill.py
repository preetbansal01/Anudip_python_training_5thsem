# Dictionary of electricity consumption
units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

# Houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:")

for house in units:
    if units[house] > 400:
        print(house)

# Find highest consumption
highest = max(units, key=units.get)
print("\nHighest Consumption:", highest, "(", units[highest], "units )")

# Find lowest consumption
lowest = min(units, key=units.get)
print("\nLowest Consumption:", lowest, "(", units[lowest], "units )")

# Calculate total units
total_units = sum(units.values())
print("\nTotal Units Consumed:", total_units)

# Lists for consumption categories
low_consumption = []
medium_consumption = []
high_consumption = []

# Categorize houses
for house in units:

    if units[house] < 200:
        low_consumption.append(house)

    elif 200 <= units[house] <= 400:
        medium_consumption.append(house)

    else:
        high_consumption.append(house)

print("\nLow Consumption:", low_consumption)
print("Medium Consumption:", medium_consumption)
print("High Consumption:", high_consumption)

# Count houses with consumption > 300
count = 0

for house in units:
    if units[house] > 300:
        count += 1

print("\nEligible for Energy-Saving Campaign:", count)