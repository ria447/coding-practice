def containsDuplicate(nums):
    
    sorted_nums = sorted(nums)
    print(sorted_nums)
    
    length = len(sorted_nums)

    for index in range(length-1):
        if length == 1:
            return False
        
        if sorted_nums[index] == sorted_nums[index + 1]:
            return True

        if index == (length - 1):
            if sorted_nums[index] == sorted_nums[index - 1]:
                return True
            else:
                return False
            
        else:
            pass

    else:
        return False
        
nums = eval(input())
output = containsDuplicate(nums)
print(output)
