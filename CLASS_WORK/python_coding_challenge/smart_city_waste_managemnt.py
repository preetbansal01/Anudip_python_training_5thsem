# Waste Data
waste = {
    "Sector1": 320,
    "Sector2": 180,
    "Sector3": 510,
    "Sector4": 275,
    "Sector5": 150,
    "Sector6": 430,
    "Sector7": 220,
    "Sector8": 390,
    "Sector9": 145,
    "Sector10": 600
}

# 1. Waste > 400
def high_waste(data):
    print("Sectors Generating More Than 400 kg Waste:", end=" ")
    for sector, val in data.items():
        if val > 400:
            print(sector, end=" ")
    print()

# 2. Max & Min waste
def max_min(data):
    max_sector = max(data, key=data.get)
    min_sector = min(data, key=data.get)

    print("\nMaximum Waste Generation:", max_sector, f"({data[max_sector]} kg)")
    print("Minimum Waste Generation:", min_sector, f"({data[min_sector]} kg)")

# 3. Total waste
def total_waste(data):
    total = sum(data.values())
    print("\nTotal Waste Collected:", total, "kg")

# 4. Categorization
def categorize(data):
    low = []
    medium = []
    high = []

    for sector, val in data.items():
        if val < 200:
            low.append(sector)
        elif 200 <= val <= 400:
            medium.append(sector)
        else:
            high.append(sector)

    print("\nLow Waste:", low)
    print("Medium Waste:", medium)
    print("High Waste:", high)

    return low, medium, high

# 5. Awareness campaign (>300)
def awareness(data):
    sectors = []
    for sector, val in data.items():
        if val > 300:
            sectors.append(sector)

    print("\nSectors Requiring Awareness Campaign:", end=" ")
    for s in sectors:
        print(s, end=" ")

    print()

    return sectors

# 6. Save to file
def save_campaign(sectors, filename):
    with open(filename, "w") as file:
        for s in sectors:
            file.write(s + "\n")

    print("\nCampaign Report Generated Successfully.")


# ---------------- MAIN ----------------

high_waste(waste)
max_min(waste)
total_waste(waste)
categorize(waste)

campaign_list = awareness(waste)
save_campaign(campaign_list, "campaign_sectors.txt")