def reverseStr(s, k):

        string = ''

        length = len(s)

        if length >= 2 * k:
            for i in range(0, length, 2 * k):
                if i == 0:
                    st = s[i + k - 1 : : -1] + s[i + k: i + 2 * k]
                    string += st
                    
                else:
                    st = s[i + k - 1 : i - 1: -1] + s[i + k: i + 2 * k]
                    
                    string += st
            return string


        if (length > k) or (length < 2  * k):
            string = s[k - 1 : : -1] + s[k : ]
            return string

        if len(s) < k:
            string = s[::-1]
            return string

s = input()
k = int(input())
output = reverseStr(s, k)
print(output)
