#first approach
def missingNumber(nums):
        List = []
        n = len(nums)
        
        for i in range(n + 1):
            List.append(i)
        
        for j in List:
            if j not in nums:
                return j
              
nums = [9,6,4,2,3,5,7,0,1]
output = missingNumber(nums)
print(output)

#second approach
def missingNumber(nums):
        n = len(nums)
        sum1 = n * (n + 1) // 2
        sum2 = sum(nums)
        return sum1-sum2
nums = [9,6,4,2,3,5,7,0,1]
output = missingNumber(nums)
print(output)
