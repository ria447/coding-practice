def myPow(x, n):
    output = float(x ** n)
    return output

x = float(input("enter the value:"))
n = int(input("enter the power:"))

result = myPow(x, n)
print(result)
