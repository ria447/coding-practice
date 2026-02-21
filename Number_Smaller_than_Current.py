def smallerNumbersThanCurrent(nums):
        
        List = []
        count = 0

        for i in nums:
            for j in nums:
                if j < i:
                    count += 1
            List.append(count)
            
            count = 0

        return List

nums = eval(input("Enter the list:"))
output = smallerNumbersThanCurrent(nums)
print(output)
