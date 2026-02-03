def strStr(self, haystack: str, needle: str) -> int:
      result = haystack.find(needle)

      return result

haystack = input("enter str:")
needle = input("enter substr:")
output = strStr(haystack, needle)
print(output)
