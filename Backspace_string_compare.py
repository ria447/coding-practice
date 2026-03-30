def backspaceCompare(s, t):
        stack_1 = []
        stack_2 = []
        str_1 = ''
        str_2 = ''

        for ch1 in s:
            if ch1 >= 'a' and ch1 <= 'z':
                stack_1.append(ch1)
            
            else:
                if len(stack_1) == 0:
                    continue
                else:
                    stack_1.pop()

        for ch2 in t:
            if ch2 >= 'a' and ch1 <= 'z':
                stack_2.append(ch2)
            
            else:
                if len(stack_2) == 0:
                    continue
                else:
                    stack_2.pop()
        
        for i in stack_1:
            str_1 += i
        for j in stack_2:
            str_2 += j

        if str_1 == str_2:
            return True
        else:
            return False

s = input()
t = input()
output = backspaceCompare(s, t)
print(output)
