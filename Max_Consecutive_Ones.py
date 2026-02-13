def findMaxConsecutiveOnes(nums):

        count = 0
        maximum = []

        for i in nums:
            if i == 1:
                count += 1
                maximum.append(count)
            else:
                maximum.append(count)
                count = 0
        
        max_consec = max(maximum)

        return max_consec
  
nums = [1,1,0,1,1,1]
output = findMaxConsecutiveOnes(nums)
print(output)
