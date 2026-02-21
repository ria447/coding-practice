# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

# Return the array in the form [x1,y1,x2,y2,...,xn,yn]

def shuffle(nums):
        
        length = len(nums)
        List_1 = []
        List_2 = []
        List = []

        for i in range(length // 2):
            List_1.append(nums[i])
        
        for j in range(length // 2, length):
            List_2.append(nums[j])

        for k in range(length // 2):
            List.append(List_1[k])
            List.append(List_2[k])
        
        return List

nums = eval(input("Enter a list:"))
output = shuffle(nums)
print(output)
