#Write a program to check whether a given number is a double number or not.
# A number is said to be a double number if:
# The total number of digits is even, and
# The first half of the number is repeated exactly in the second half.
# Examples:
# 1212 → double number (12 is repeated)
# 1234 → not a double number
number = int(input("Enter a number:"))
string = str(number)

number = 0
length = len(string)
if length % 2 != 0:
    print("not a double number")
else:
    num_length = int(length / 2)
    for i in string[0: num_length]:
        if string.count(i) == num_length:
            number += 1

    if number == num_length:
        print("a double number")
    else:
        print("not a double number")
