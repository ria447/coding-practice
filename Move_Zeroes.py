def moveZeroes(nums):
      
        list_1 = []
        list_2 = []

        for i in nums:
            if i == 0:
                list_2.append(i)
            else:
                list_1.append(i)
        
        List = list_1 + list_2
        nums.clear()
        nums = nums.extend(List)
        return nums

nums = eval(input("Enter the list:"))
output = moveZeroes(nums)
print(output)
