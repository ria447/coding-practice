import math 

def mySqrt(x):
  if x > 0:
    return int(math.sqrt(x))
    
x = int(input("Enter a number:"))
result = mySqrt(x)
print(result)
