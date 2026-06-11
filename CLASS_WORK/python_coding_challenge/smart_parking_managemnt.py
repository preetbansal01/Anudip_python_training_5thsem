# Parking Slot Management System

parking_slots = [
    "Occupied", "Vacant", "Occupied", "Vacant",
    "Occupied", "Occupied", "Vacant", "Occupied",
    "Vacant", "Occupied"
]

# 1. Display vacant slots
def display_vacant(slots):
    vacant = []
    for i in range(len(slots)):
        if slots[i] == "Vacant":
            vacant.append(i + 1)

    print("Vacant Parking Slots:", *vacant)
    return vacant


# 2. Count occupied and vacant
def count_slots(slots):
    occupied = 0
    vacant = 0

    for s in slots:
        if s == "Occupied":
            occupied += 1
        else:
            vacant += 1

    print("Occupied Slots:", occupied)
    print("Vacant Slots:", vacant)


# 3. Allocate first vacant slot
def allocate_slot(slots):
    for i in range(len(slots)):
        if slots[i] == "Vacant":
            slots[i] = "Occupied"
            print(f"Vehicle Allocated to Slot {i + 1}")
            return
    print("No Vacant Slot Available")


# 4. Calculate occupancy percentage
def occupancy_percentage(slots):
    occupied = slots.count("Occupied")
    percent = (occupied / len(slots)) * 100
    print(f"Occupancy Percentage: {percent:.1f}%")


# 5. Save to file
def save_to_file(parking_slots, "parking.txt")
    with open( parjing.txt, "w") as file:
        for i in range(len(slots)):
            file.write(f"Slot {i+1}: {slots[i]}\n")

    print("Parking Details Saved Successfully.")


# ---------------- MAIN PROGRAM ----------------

vacant = display_vacant(parking_slots)
count_slots(parking_slots)
allocate_slot(parking_slots)
occupancy_percentage(parking_slots)
save_to_file(parking_slots, "parking.txt")