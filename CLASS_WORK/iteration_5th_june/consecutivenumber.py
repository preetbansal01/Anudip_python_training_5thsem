# List of numbers
numbers = [4, 5, 6, 10, 11, 15, 16, 17]

# List to store consecutive pairs
consecutive_pairs = []

# Check consecutive numbers
for i in range(len(numbers) - 1):

    # If difference is 1, numbers are consecutive
    if numbers[i + 1] - numbers[i] == 1:

        print(numbers[i], "and", numbers[i + 1], "are consecutive")

        # Store pair in list
        consecutive_pairs.append((numbers[i], numbers[i + 1]))

# Display all pairs
print("Consecutive Pairs:", consecutive_pairs)

#Start.
# Create a list of numbers.
# Create an empty list consecutive_pairs to store consecutive pairs.
# Traverse the list from the first element to the second-last element.
# For each element:
# Compare it with the next element.
# If the difference between them is 1, then:
# Print that the numbers are consecutive.
# Store the pair in consecutive_pairs.
# After the loop ends, print consecutive_pairs.
# Stop.