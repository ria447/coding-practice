def canMakeArithmeticProgression(arr):
        arr.sort()

        count = 0
        if len(arr) >= 3:
            for i in range(len(arr) - 2):
            
                if arr[i + 1] - arr[i] == arr[i + 2] - arr[i + 1]:
                        count += 1
                
                else:
                    return False

        if len(arr) < 3:
            return True
            
        if count == (len(arr) - 2):
            return True

arr = eval(input("enter list:"))
output = canMakeArithmeticProgression(arr)
print(output)
