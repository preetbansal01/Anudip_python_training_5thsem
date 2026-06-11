# Water Usage Data
water_usage = {
    "House101": 1800,
    "House102": 2200,
    "House103": 3500,
    "House104": 2800,
    "House105": 1600,
    "House106": 4100,
    "House107": 2400,
    "House108": 3900,
    "House109": 1500,
    "House110": 4500
}

# 1. Houses consuming more than 3000 litres
def high_consumers(data):
    print("Houses Consuming More Than 3000 Litres:", end=" ")

    for house, usage in data.items():
        if usage > 3000:
            print(house, end=" ")

    print()


# 2. Highest and lowest consumers
def highest_lowest(data):
    highest_house = max(data, key=data.get)
    lowest_house = min(data, key=data.get)

    print("\nHighest Consumption:", highest_house, f"({data[highest_house]} litres)")
    print("Lowest Consumption:", lowest_house, f"({data[lowest_house]} litres)")


# 3. Total consumption
def total_consumption(data):
    total = sum(data.values())
    print("\nTotal Consumption:", f"{total:,}", "litres")


# 4. Categorization
def categorize(data):
    low = []
    medium = []
    high = []

    for house, usage in data.items():
        if usage < 2000:
            low.append(house)
        elif 2000 <= usage <= 3500:
            medium.append(house)
        else:
            high.append(house)

    print("\nLow Consumption:", low)
    print("Medium Consumption:", medium)
    print("High Consumption:", high)

    return low, medium, high


# 5. Eligible households (>2500 litres)
def eligible_households(data):
    count = 0

    for usage in data.values():
        if usage > 2500:
            count += 1

    print("\nEligible Households:", count)


# ---------------- MAIN PROGRAM ----------------

high_consumers(water_usage)
highest_lowest(water_usage)
total_consumption(water_usage)
categorize(water_usage)
eligible_households(water_usage)