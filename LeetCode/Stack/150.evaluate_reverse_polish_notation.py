class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        stk=[]

        for token in tokens:
            if token not in ['+','-','*','/']:
                stk.append(token)
            else:
                second = stk.pop()
                first = stk.pop()

                second, first = int(second), int(first)

                if token == '+':
                    val = first + second 
                elif token == '-':
                    val = first - second
                elif token == '*':
                    val = first * second
                elif token == '/':
                    val = int (first/second) 
                
                stk.append(val)
        
        return stk[0]

# T: O(n), 
# S: O(1)