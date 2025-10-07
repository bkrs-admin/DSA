from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # ransom_count = Counter(ransomNote)
        # magazine_count = Counter(magazine)

        # # for char, cnt in ransom_count.items():
        # #     if magazine_count[char] < cnt:
        # #         return False
        
        # # return True

        # return not(ransom_count - magazine_count)

        h_map = {}

        for c in magazine:
            h_map[c] = h_map.get(c, 0) + 1

        for c in ransomNote:
            if c not in h_map or h_map[c] == 0:
                return False
            h_map[c] -= 1
        
        return True

# T: O(m + n)
# T: O(n)

# ✅ Approach 1 — Using Counter Subtraction
# 💬 Interview Explanation

# I use two Counters to store character frequencies for both strings.
# Then I subtract them — if the result is empty, it means the magazine has enough characters for the ransom note.

# This is clean and Pythonic, running in O(n + m) time and O(1) space since there are only 26 lowercase letters.

# ⏱ Time: O(n + m)
# 💾 Space: O(1) (bounded by alphabet size)

# ✅ Approach 2 — Manual Frequency Comparison
# 💬 Interview Explanation

# I count the frequency of each character in both strings using Counter.
# Then I check whether every character in the ransom note appears at least as many times in the magazine.

# This is intuitive and efficient — O(n + m) time and constant space.

# ⏱ Time: O(n + m)
# 💾 Space: O(1)

# ✅ Approach 3 — Greedy Character Reduction
# 💬 Interview Explanation

# I build a frequency map for the magazine, then iterate through each character in the ransom note.
# For every match, I decrement the count — if any character runs out, I return False early.

# This is slightly more manual but very clear, still O(n + m) time and O(1) space.

# ⏱ Time: O(n + m)
# 💾 Space: O(1)