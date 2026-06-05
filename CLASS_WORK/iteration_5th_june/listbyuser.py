#list = []

#for i in range (20):
 #   entry = int(input("enter the user {i}"))
  #  print (entry)
   # list.append(entry)

#unique_list = list(set(list))

#print(list)

#
numbers = []

for i in range(20):
    entry = int(input(f"Enter number {i+1}: "))
    numbers.append(entry)

num = int(input("Enter the number to remove : "))

count = 0
new_list = []

for x in numbers:
    if x == num:
        count += 1
        if count == 1:
            new_list.append(x)
    else:
        new_list.append(x)

print(new_list)