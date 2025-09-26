def rotateLeft(d, arr):
    return arr[d:] + arr[:d]

d = 4
ar = [1,2,3,4,5]
a = rotateLeft(d, ar)

print(a) #expected [5,1,2,3,4]

# Time and Space complexity
# T: O(n), length of arr
# S: O(n), size of arr