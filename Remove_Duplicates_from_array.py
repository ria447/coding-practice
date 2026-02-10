def removeDuplicates(nums):
        
        List_2 = []
        List_1 = []

        previous_element = nums[0]
        List_1.append(previous_element)
        
        for i in nums[1:]:
            if i != previous_element:
                List_1.append(i)
                previous_element = i
            else:
                List_2.append('_')
            
        nums.clear()
        nums.extend(List_1)
        k = len(nums)
        List_3 = nums + List_2
        nums = List_3
    
        return k

nums = eval(input("Enter a list"))
Output = removeDuplicates(nums)
print(output)
