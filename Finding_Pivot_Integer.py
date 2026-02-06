def pivotInteger(n):

        sum_1 = 0
        sum_2 = 0

        if n == 1:
            return 1
        
        for i in range(1, n + 1):
            
            sum_1 = sum_1 + i
            for j in range(i, n + 1):
                sum_2 = sum_2 + j
            if sum_1 == sum_2:
                return i
            else:
                sum_2 = 0
                
        else:
            return -1

n = int(input("enter a number:"))
output = pivotInteger(n)
print(output)
