''' Example:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.  '''

def fib(n):
        
        fibo_list = [0, 1]
    
        for i in range(2, n + 1):
            next_elemen = fibo_list[i-1] + fibo_list[i-2]
            fibo_list.append(next_elemen)

        return fibo_list[n]

n= int(input("enter a number:"))
output = fib(n)
print(output)
