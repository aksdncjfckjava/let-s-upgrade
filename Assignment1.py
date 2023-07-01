# Create a list with 10 index values
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Print the original list
print("Original list:", my_list)

# Add two new values to the list
my_list.append(10)
my_list.append(11)

# Print the updated list
print("List after adding new values:", my_list)

# Delete three values from the list
del my_list[2]
del my_list[4]
del my_list[6]

# Print the list after deletion
print("List after deleting values:", my_list)

# Slice the list
sliced_list = my_list[2:7]

# Print the sliced list
print("Sliced list:", sliced_list)
