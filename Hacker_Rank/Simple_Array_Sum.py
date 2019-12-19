"""
Calculate the sum of integers in an array.
"""

array = [1, 2, 3, 4, 5, 6]
sum_of_array = 0
for i in range(len(array)):
    sum_of_array += array[i]
print("\nThe sum of integers in the array:", sum_of_array)
