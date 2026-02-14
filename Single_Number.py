def singleNumber(nums)t:
        
        for i in nums:
            if nums.count(i) != 2 :                   #O(N^2)
                return i
                break

nums = eval(input("Enter a list:"))
output = singleNumber(nums)
print(output)
