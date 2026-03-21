# using count()

def findLucky(arr):
        
        lucky_int = []

        for i in arr:
            if arr.count(i) == i:
                lucky_int.append(i)
        
        if lucky_int == []:
            return -1
        else:
            return max(lucky_int)

arr = eval(input())
output = findLucky(arr)
print(output)
