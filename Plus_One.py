def plusOne(digits):
        string_1 = ''
        string_2 = ''
        List = []

        for i in digits:
            string_1 = string_1 + str(i)
        
        summation = int(string_1) + 1
        string_2 = string_2 + str(summation)

        for i in string_2:
            List.append(int(i))
        
        return List

digits = eval(input("enter a list:"))
output = plusOne(digits)
print(output)
