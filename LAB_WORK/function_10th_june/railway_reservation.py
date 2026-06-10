seats = [
    "Booked", "Available", "Booked", "Booked",
    "Available", "Available", "Booked", "Available",
    "Booked", "Booked", "Available", "Booked"
]

# 1. Count booked and available seats
def count_seats(seats):
    booked = seats.count("Booked")
    available = seats.count("Available")
    return booked, available

# 2. Find first available seat
def first_available(seats):
    for i, seat in enumerate(seats, start=1):
        if seat == "Available":
            return i
    return None

# 3. Calculate occupancy percentage
def occupancy_percentage(seats):
    booked = seats.count("Booked")
    return (booked / len(seats)) * 100

# 4. Display all available seat numbers
def display_available_seats(seats):
    available_seats = []
    for i, seat in enumerate(seats, start=1):
        if seat == "Available":
            available_seats.append(i)
    return available_seats


# Driver Code
booked, available = count_seats(seats)
print("Booked Seats:", booked)
print("Available Seats:", available)

print("\nFirst Available Seat:", first_available(seats))

print("\nOccupancy Percentage: {:.2f}%".format(
    occupancy_percentage(seats)
))

print("\nAvailable Seat Numbers:", *display_available_seats(seats))
print("")