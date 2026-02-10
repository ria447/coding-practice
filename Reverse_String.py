def reverseString(s):
       
        nums = s[::-1]
        s.clear()
        s.extend(nums)
        return s

s = eval(input("Enter the list:"))
output = reverseString(s)
print(output)
