# Create a list with duplicates
my_list = [1, 2, 3, 3, 4, 5, 5, 6, 6]

# Convert the list to a set to remove duplicates
my_set = set(my_list)

# Convert the set back to a list
my_list_without_duplicates = list(my_set)

# Print the original list, set, and list without duplicates
print("Original list:", my_list)
print("Set without duplicates:", my_set)
print("List without duplicates:", my_list_without_duplicates)
