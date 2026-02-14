def isPowerOfTwo(n):

        if n == 1:
            return True

        if n <= 0:
            return False
        
        while n > 1:
            if n % 2 == 0:
                n = n // 2
            
            else:
                return False
        
        if n == 1:
            return True

n = int(input("Enter a number"))
output = isPowerOfTwo(n)
print(output)
