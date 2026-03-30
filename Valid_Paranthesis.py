def isValid(s):
        
        stack = []
        if len(s) % 2 != 0:
            return False

        if s[0] in '}])':
            return False

        for char in s:
            if char in '[{(':
                stack.append(char)
            
            else:
                if len(stack) != 0:
                    top = stack.pop()
                else:
                    return False
                

                if char == ']' and top != '[':
                    return False
                elif char == '}' and top != '{':
                    return False
                elif char == ')' and top != '(':
                    return False

        if len(stack) == 0:
            return True
        else:
            return False

s = input()
output = isValid(s)
print(output)
