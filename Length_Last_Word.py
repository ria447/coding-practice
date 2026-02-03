def lengthOfLastWord(s):
        
      words = s.split()
      length = len(words[-1])

      return length

s = input("enter a string:")
output = lengthOfLastWord(s)
print(output)
