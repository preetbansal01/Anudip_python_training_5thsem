runs = {     "Virat": 645,     "Rohit": 512,     "Gill": 698,     "Rahul": 435,     "Hardik": 278,     "Pant": 534,     "Surya": 389,     "Jadeja": 301,     "Iyer": 455,     "KL": 410 } 
print("player score more tham 50 :")
for i in runs:
    if runs[i] > 500 :
        print[i]

#2. orange cap winner
orange_cap = max(runs, key=runs.get)
print("\nOrange Cap Winner:", orange_cap, "(", runs[orange_cap], ")")

# Find lowest scorer
lowest = min(runs, key=runs.get)
print("\nLowest Scorer:", lowest, "(", runs[lowest], ")")

# Calculate total runs
total_runs = sum(runs.values())
print("\nTotal Tournament Runs:", total_runs)

# Players scoring below 400
below_400 = []

for player in runs:
    if runs[player] < 400:
        below_400.append(player)

print("\nPlayers Scoring Below 400:", below_400)

# Count players scoring between 400 and 600
count = 0

for player in runs:
    if 400 <= runs[player] <= 600:
        count += 1

print("\nPlayers Between 400 and 600 Runs:", count)