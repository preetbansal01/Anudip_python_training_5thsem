temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

# 1. Cities having temperature above 40°C
print("Cities Above 40°C:")
for city in temperature:
    if temperature[city] > 40:
        print(city)

# 2. Hottest city
hottest = max(temperature, key=temperature.get)
print("\nHottest City:", hottest, "(", temperature[hottest], "°C )")

# 3. Coolest city
coolest = min(temperature, key=temperature.get)
print("\nCoolest City:", coolest, "(", temperature[coolest], "°C )")

# 4. Average temperature
total = sum(temperature.values())
average = total / len(temperature)
print("\nAverage Temperature:", average, "°C")

# 5. Pleasant cities (temperature < 35°C)
pleasant = []

for city in temperature:
    if temperature[city] < 35:
        pleasant.append(city)

print("\nPleasant Cities:", pleasant)

# 6. Count cities with temperature between 35°C and 40°C
count = 0

for city in temperature:
    if temperature[city] >= 35 and temperature[city] <= 40:
        count += 1

print("\nCities Between 35°C and 40°C:", count)