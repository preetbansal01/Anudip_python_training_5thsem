# Classwork : To read the data from file and display the following:
# 1. No. of Vowels in file.
# 2. No. of characters into the file. 
# 3. No. of lines into the file.

# Open file in read mode
# Open file in read mode
file = open(r"C:\Users\gujja\OneDrive\Desktop\PYTHON ANUDEEP\CLASS_WORK\file_handling_10_june\file.txt", "r")

text = file.read()

# 1. Count vowels
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in text if char in vowels)

# 2. Count characters
char_count = len(text)

# 3. Count lines
line_count = len(text.splitlines())

file.close()

# Display results
print("Number of vowels:", vowel_count)
print("Number of characters:", char_count)
print("Number of lines:", line_count)
