# Program to perform union, intersection,
# symmetric difference, and subset operations.

# Taking input for first set
set1 = set(map(int, input("Enter elements of Set 1 separated by space: ").split()))

# Taking input for second set
set2 = set(map(int, input("Enter elements of Set 2 separated by space: ").split()))

# Performing operations
union_result = set1.union(set2)
intersection_result = set1.intersection(set2)
symmetric_difference_result = set1.symmetric_difference(set2)

# Displaying results
print("\nUnion:", union_result)
print("Intersection:", intersection_result)
print("Symmetric Difference:", symmetric_difference_result)

# Checking subset
if set1.issubset(set2):
    print("Set 1 is a subset of Set 2")

elif set2.issubset(set1):
    print("Set 2 is a subset of Set 1")

else:
    print("No set is a subset of the other")

# Expected Output
"""
Example Input:
Set 1: 1 2 3 4
Set 2: 3 4 5 6

Expected Output:
Union: {1, 2, 3, 4, 5, 6}
Intersection: {3, 4}
Symmetric Difference: {1, 2, 5, 6}
No set is a subset of the other
"""