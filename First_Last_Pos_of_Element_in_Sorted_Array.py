def searchRange(nums, target):
        
        List = []
        output_list = []

        if target in nums:
            for i in range(len(nums)):
                if nums[i] == target:
                    
                    List.append(i)
                    print(List)

            output_list.append(List[0])
            output_list.append(List[-1])

            return output_list
        else:
            List = [-1, -1]
            return List

        if nums.isempty():
            return [-1, -1]
        
nums = eval(input("Enter a sorted list:"))
target = int(input("Enter the number you want the first and last position for"))
output = searchRange(nums, target)
print(output)
