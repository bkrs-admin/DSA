
def twoSum(numbers, target):
    h_map = {}

    for i, val in enumerate(numbers):
        diff = target - val
        if diff in h_map:
            return [h_map[diff] + 1, i+1]
        else:
            h_map[val] = i


    return []

# T: O(n)
# T: O(n)


# I’m finding two numbers that add up to the target.

# I use a hash map to store each number and its index.
# For every element, I check if the complement (target - num) is already in the map — if so, I return both indices.

# This approach takes O(n) time and O(n) space since we store up to all elements in the hash map.

# | Concept              | Explanation                                                                        |
# | -------------------- | ---------------------------------------------------------------------------------- |
# | **Approach**         | Hash map lookup (`diff in h_map`)                                                  |
# | **Why it works**     | Each number is checked once; complements are found in constant time                |
# | **Time Complexity**  | O(n)                                                                               |
# | **Space Complexity** | O(n)                                                                               |
# | **Alternative**      | For a **sorted** array, use the **two-pointer** technique (O(n) time, O(1) space). |
