class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz",

        }

        res, curr = [], []

        def dfs(index):
            if len(curr) == len(digits):
                res.append("".join(curr))
                return
            
            digit = digits[index]

            letter = phone_map[digit]
            
            for c in letter:
                curr.append(c)
                dfs(index + 1)
                print(curr)
                curr.pop()

        dfs(0)
        return res
# T: O(n^2)
# S: O(n)