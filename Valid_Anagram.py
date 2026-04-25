# time efficient
def isAnagram(s, t):

        sums = 0
        
        if len(s) != len(t):
            return False
        
        else:
            set_s = set(s)

            for i in set_s:
                if s.count(i) != t.count(i):
                    return False
            return True
s = input("Enter first string: ")
t - input("Enter second string: ")
output = isAnagram(s, t)
print(output)



# slower
def isAnagram(s, t):

        sums = 0
        
        if len(s) != len(t):
            return False
        
        else:
            for i in s:
                if s.count(i) == t.count(i):
                    sums += 1
        
            if sums == len(s):
                return True
            else:
                return False
s = input("Enter first string: ")
t - input("Enter second string: ")
output = isAnagram(s, t)
print(output)
    
