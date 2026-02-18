def sortedSquares(nums):
        
        List = []

        for i in nums:
            List.append(i ** 2)
        
        List.sort()

        return List

nums = eval(input("Enter a list:"))
output = sortedSquares(nums)
print(output)
