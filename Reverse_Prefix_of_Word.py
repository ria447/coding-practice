def reversePrefix(word, ch):
        
        reversed_word = ''
        index = word.find(ch)

        for i in range(index, -1, -1):
            reversed_word += word[i]
        
        for i in range(index + 1, len(word)):
            reversed_word += word[i]

        return reversed_word

word = input()
ch = input()
output = reversePrefix(word, ch)
print(output)
