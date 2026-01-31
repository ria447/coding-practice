def armstrong_number(number):
    
    string = str(number)
    length = len(string)
    sum = 0

    for digit in string:

        sum = sum + int(digit) ** length

    if sum == number:
        return "Armstrong Number"
    
    else:
        return "Not an Armstrong Number"
    
number = int(input("Enter a number:"))
output = armstrong_number(number)
print(output)
