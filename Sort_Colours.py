def sortColors(nums):
       
        sort_list = []
        for i in nums:
            if i == 0:
                sort_list.append(i)
        for i in nums:
            if i == 1:
                sort_list.append(i)
        for i in nums:
            if i == 2:
                sort_list.append(i)
  
        nums.clear()
        #print(sort_list)
        nums.extend(sort_list)
        return nums

nums = eval(input("enter a list:"))
output = sortColors(nums)
print(output)
