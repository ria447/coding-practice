def merge(self, nums1, m, nums2, n):
        
        new_list = nums1[:m] + nums2[:n]

        sorted_list = sorted(new_list)
        nums1[:] = sorted_list

        return nums1

nums1 = eval(input())
nums2 = eval(input())
m = 0
n = 0

for i in nums1:
    if i != 0:
         m += 1
    
for j in nums2:
    if j != 0:
         n += 1

output = merge(nums1, m, nums2, n)
print(output)
