import numpy as np

# Create a one-dimensional array containing numbers from 1 to 10.
numbers = np.arange(1, 11)
print("Original array:", numbers)
print("Shape:", numbers.shape)
print("Data type:", numbers.dtype)

# Indexing and slicing
print("First element:", numbers[0])
print("Last three elements:", numbers[-3:])
print("Elements at even positions:", numbers[::2])

# Mathematical operations (element-wise)
print("Array + 5:", numbers + 5)
print("Array * 2:", numbers * 2)
print("Squares:", numbers ** 2)
print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))

# Sorting and concatenation
unsorted = np.array([5, 2, 8, 1])
print("Sorted:", np.sort(unsorted))
print("Concatenated:", np.concatenate((numbers, np.array([11, 12]))))
