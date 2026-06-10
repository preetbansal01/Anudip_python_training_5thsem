# Program to copy content from one file to another
 
# Open source file in read mode
source_file = open(r"C:\Users\gujja\OneDrive\Desktop\PYTHON ANUDEEP\CLASS_WORK\file_handling_10_june\file.txt", "r")

# Read all content
data = source_file.read()

# Close source file
source_file.close()

# Open destination file in write mode
destination_file = open(r"C:\Users\gujja\OneDrive\Desktop\PYTHON ANUDEEP\CLASS_WORK\file_handling_10_june\copy_file.txt", "w")

# Write content into destination file
destination_file.write(data)

# Close destination file
destination_file.close()

print("File copied successfully!")
