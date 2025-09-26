# Array - Mutable(changeable)
# Peek - O(1) arr[i]
# Search - O(n)
# Insert - O(n)
# Delete - O(n)

# Static vs dynamic array 
# Python only have dynamic arrays / list

# Appending to end O(1) (amortized, average)
# Popping(delete) from end O(1)
# Insert/deletion not from end O(n)
# Modifying an element O(1)
# Random access O(1)
# Search - Checking if element exists O(n) 

# Strings - immutable(unchangeable)
# In order to change, abc + d
# Random access - O(1), other operations - O(n)


# ex)
a = [1, 2, 3]

print(a)
# expected [1,2,3]

# Append - Insert element at end of array - on average - O(1)
a.append(5)

print(a)
# expected [1,2,3,5]

# Pop - Deleting element at end of array - O(1)
a.pop()

print(a)
# expected [1,2,3]

# Insert (not at end of array) - O(n)
# .insert(index, element)
a.insert(2, 5)

print(a)
# expected [1,2,5,3]

# Modify an element - O(1)
a[0] = 7

print(a)
# expected [7,2,5,3]

# Accessing element given index i - O(1)
print(a[2])
# expected 5

if 7 in a:
  print(True)
# expected True

#################################################
#Strings 

# Append to end of stings
s = "hello"
b = s + "z"

print(b)
# expected helloz

# Check if something is in string
if 'h' in s:
  print(True)
  # expected True

# length of array/strings - O(1)
print(len(a)) # expected 4
print(len(b)) # expected 6