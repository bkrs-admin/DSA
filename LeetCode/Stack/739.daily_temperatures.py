class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stk = []

        for index, temp in enumerate(temperatures):
            while stk and temperatures[stk[-1]] < temp:
                prev = stk.pop()

                res[prev] = index - prev

            stk.append(index)
        
        return res
    
# T: O(n), 
# S: O(n)