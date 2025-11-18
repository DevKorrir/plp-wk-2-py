# 1. Create an empty list
my_list = []

# 2. Append elements (10, 20, 30, 40)
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(f"After Append: {my_list}")

# 3. Insert 15 at the second position
# Note: Python uses 0-based indexing, so index 1 is the second position.
my_list.insert(1, 15)
print(f"After Insert: {my_list}")

# 4. Extend with another list [50, 60, 70]
# .extend() adds multiple items at once.
my_list.extend([50, 60, 70])
print(f"After Extend: {my_list}")

# 5. Remove the last element
# .pop() removes the last item by default if no index is given.
my_list.pop()
print(f"After Pop:    {my_list}")

# 6. Sort in ascending order
my_list.sort()
print(f"After Sort:   {my_list}")

# 7. Find and print the index of 30
index_of_30 = my_list.index(30)

print("-" * 20)
print(f"The index of 30 is: {index_of_30}")