# Seat status
seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

# Counters
booked = 0
available = 0

# List for available seat numbers
available_seats = []

# Count booked and available seats
for i in range(len(seats)):

    if seats[i] == 1:
        booked += 1

    else:
        available += 1
        available_seats.append(i + 1)   # Seat number

# Find first available seat
for i in range(len(seats)):

    if seats[i] == 0:
        first_available = i + 1
        break

# Calculate occupancy percentage
occupancy = (booked / len(seats)) * 100

# Display results
print("Booked Seats:", booked)
print("Available Seats:", available)
print("First Available Seat:", first_available)
print("Available Seat Numbers:", available_seats)

if occupancy > 70:
    print("Bus is more than 70% occupied")
else:
    print("Bus is not more than 70% occupied")