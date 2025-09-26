def reverseArray(a):
    return a[::-1]

arr = [1,2,3]
a = reverseArray(arr)

print(a) # expected [3,2,1]

# T and S complexity
# T: O(n)
# S: O(n)

# S can be optimized using two pointers