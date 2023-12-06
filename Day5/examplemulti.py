import numpy as np

# Define the dimensions of the multi-dimensional arrays
rows = 3
columns = 4
depth = 2

# Initialize the dictionary
multi_dict = {}

# Populate the dictionary with multi-dimensional arrays
for i in range(rows):
    for j in range(columns):
        for k in range(depth):
            key = (i, j, k)
            array_shape = (5, 5, 5)  # Adjust the shape of the multi-dimensional array as needed
            multi_dict[key] = np.zeros(array_shape)

# Accessing an example element in the dictionary
example_key = (1, 2, 0)
example_array = multi_dict[example_key]

# Print the initialized dictionary and an example array
print("Initialized Dictionary:")
print(multi_dict)
print("\nExample Array for key", example_key, ":")
print(example_array)