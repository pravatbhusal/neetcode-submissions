class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        para_dict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        open_parans = para_dict.keys()
        closed_parans = para_dict.values()

        for char in s:
            if char in open_parans:
                # append open paranthesis
                stack.append(char)
            elif char in closed_parans and len(stack) != 0:
                # pop stack and check paranthesis
                open_para = stack.pop()
                if para_dict[open_para] != char:
                    # invalid open/closed paranthesis
                    return False
            else:
                # invalid char
                return False
        
        # if stack empty, paranthesis are balanced
        return len(stack) == 0
        

        