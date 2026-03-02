# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

def findDisappearedNumbers(nums):
        
        length = len(nums)
        nums_set = set(nums)
        List = []
        result = []

        for i in range(1, length + 1):
            
            if i not in nums_set:
                result.append(i)
        
        return result

nums = eval(input("enter a list:"))
output = findDisappearedNumbers(nums)
print(output)
