import math
def mySqrt(x):
    # edge case handling
    if x == 1:
        return 1

    left, right = 0, x - 1 # two pointer for binary searching
    ans = 0 # tmp variable for storing answer
    while left <= right:
        mid = left + (right - left) // 2 # mid pointer with prevent integer overflow

        if mid * mid == x: # if mid^2 == x, return x with round down to nearest int
            return math.floor(mid)
        elif mid * mid < x: # if smaller than x, then store mid to potential ans and move left pointer
            ans = mid
            left = mid + 1
        else:               # if greater than x, then move right pointer to mid -1
            right = mid - 1

    return math.floor(ans) # return ans with round down to nearest int

# T: O(log n)
# S: O(1)