class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # in order to get "longest" substring length without duplicate, we use sliding window and hashsett to prevent duplicate

        # the core logic is window is expanding up until duplication found
        # then remove duplication and movin left += 1
        # if not found, then add it to hashset and keep updated longest length 

        # left pointer to 0
        left = 0
        # n for length of given string
        n = len(s)
        # sett for hashset 
        sett = set()
        # longest to store longest length
        longest = 0

        # we are going to iterate n times, uisng index as right pointer to expand
        for right in range(n):
            #first, check if you have any duplicate in sett first,
            while s[right] in sett:
                #then remove it from left to shrink the window size
                sett.remove(s[left])
                #move left pointer + 1
                left += 1
            
            #if no duplicate in sett, then add it to sett
            sett.add(s[right])
            # get and update window size with longest using max function to compare
            window = (right - left) + 1
            longest = max(longest, window)

        return longest
  
  # T: O(n)
  # S: O(n)