class Solution:
    def isPalindrome(self, x:int) -> bool:
        string = str(x)
        if x < 0:
            return False
        return string == string[::-1]
