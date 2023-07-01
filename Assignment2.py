# Create an empty dictionary
my_dict = {}

# Add key-value pairs to the dictionary
my_dict["name"] = "John"
my_dict["age"] = 25
my_dict["city"] = "New York"

# Print the dictionary
print("Original dictionary:", my_dict)

# Delete key-value pairs from the dictionary
del my_dict["age"]
my_dict.pop("city")

# Print the updated dictionary
print("Dictionary after deleting key-value pairs:", my_dict)
