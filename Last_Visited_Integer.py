def lastVisitedIntegers(nums):
        seen = []
        ans = []
        k = 0

        for i in nums:
            if i >= 0:
                seen.append(i)

                k = 0
        
            if i < 0:
                k += 1
                
                if k <= len(seen):
                    ans.append(seen[-k])
                else:
                    ans.append(-1)

        return ans

nums = eval(input())
output = lastVistedIntegers(nums)
print(output)
