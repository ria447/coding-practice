def search(nums, target):
        
        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2

        while start <= end:
            if nums[mid] == target:
                return nums.index(target)
            if target > nums[mid]:
                start = mid + 1
                mid = (start + end) // 2
            if target < nums[mid]:
                end = mid - 1
                mid = (start + end) // 2
            
        else:
            return -1

nums = eval(input("enter a list:"))
target = int(input("Enter the number you want to search for in the list:"))
output = search(nums, target)
print(output)
