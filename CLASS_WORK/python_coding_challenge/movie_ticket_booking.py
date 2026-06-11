# Seat Booking System

tickets = {
    "A1": "Booked",
    "A2": "Available",
    "A3": "Booked",
    "A4": "Available",
    "B1": "Booked",
    "B2": "Available",
    "B3": "Booked",
    "B4": "Available",
    "C1": "Booked",
    "C2": "Available"
}

# 1. Display available seats
def display_available(tickets):
    available = []

    for seat, status in tickets.items():
        if status == "Available":
            available.append(seat)

    print("Available Seats:", *available)
    return available


# 2. Count booked and available seats
def count_seats(tickets):
    booked = 0
    available = 0

    for status in tickets.values():
        if status == "Booked":
            booked += 1
        else:
            available += 1

    print("\nBooked Seats:", booked)
    print("Available Seats:", available)

    return booked, available


# 3. Reserve first available seat
def reserve_seat(tickets):
    for seat in tickets:
        if tickets[seat] == "Available":
            tickets[seat] = "Booked"
            print(f"\nSeat {seat} Reserved Successfully.")
            return seat


# 4. Save updated data to file
def save_to_file(tickets, filename):
    with open(filename, "w") as file:
        for seat, status in tickets.items():
            file.write(f"{seat}:{status}\n")

    print("\nBooking Details Saved Successfully.")


# 5. Occupancy percentage
def occupancy_percentage(tickets):
    total = len(tickets)
    booked = list(tickets.values()).count("Booked")

    percent = (booked / total) * 100
    print(f"\nHall Occupancy Percentage: {percent:.1f}%")


# ---------------- MAIN PROGRAM ----------------

available = display_available(tickets)
count_seats(tickets)

reserve_seat(tickets)

occupancy_percentage(tickets)

save_to_file(tickets, "tickets.txt")