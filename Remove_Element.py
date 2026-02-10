def removeElement(nums, val):
        
        length = len(nums)
        list_1 = []
        list_2 = []

        for i in nums:
            if i != val:
                list_1.append(i)
            else:
                list_2.append('_')
            
        nums.clear()
        nums.extend(list_1)
        k = len(nums)

        list_3 = nums + list_2

        return k

nums = eval(input("Enter the list:"))
val = int(input("Enter a number:"))
output = removeElement(nums, val)
print(output)
                  
