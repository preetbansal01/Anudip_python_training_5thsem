# Input scores of 11 players without using list
for i in range(1, 12):
    score = int(input(f"Enter score of player {i}: "))
    if i == 1:
        p1 = score
    elif i == 2:
        p2 = score
    elif i == 3:
        p3 = score
    elif i == 4:
        p4 = score
    elif i == 5:
        p5 = score
    elif i == 6:
        p6 = score
    elif i == 7:
        p7 = score
    elif i == 8:
        p8 = score
    elif i == 9:
        p9 = score
    elif i == 10:
        p10 = score
    elif i == 11:
        p11 = score
# Display scores
print("\nScores of 11 players:")
print("Player 1:", p1)
print("Player 2:", p2)
print("Player 3:", p3)
print("Player 4:", p4)
print("Player 5:", p5)
print("Player 6:", p6)
print("Player 7:", p7)
print("Player 8:", p8)
print("Player 9:", p9)
print("Player 10:", p10)
print("Player 11:", p11)
