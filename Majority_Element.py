from collections import Counter

    def majorityElement(nums):

        dictionary = Counter(nums)

        frequency = list(dictionary.values())[0]
        majority_number = 0

        for i in dictionary:
            if dictionary[i] >= frequency:
                frequency = dictionary[i]
                majority_number = i
        
        return majority_number

nums = eval(input())
output = majorityElement(nums)
print(output)        
