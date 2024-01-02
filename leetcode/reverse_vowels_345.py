# leetcode url: https://leetcode.com/problems/reverse-vowels-of-a-string/

# leetcode problem: 345
# Description: Write a function that takes a string as input and reverse only the vowels of a string.


class Solution:
    def reverseVowels(self, s: str) -> str:
        # create a list of vowels
        vowels = ['a', 'e', 'i', 'o', 'u']
        # create a list of the vowels in the string
        vowel_list = []
        # iterate over the string
        for i in range(len(s)):
            # check if the character is a vowel
            if s[i].lower() in vowels:
                # append the vowel to the list
                vowel_list.append(s[i])
        # create a new string
        new_string = ''
        # iterate over the string
        for i in range(len(s)):
            # check if the character is a vowel
            if s[i].lower() in vowels:
                # add the last vowel to the string
                new_string += vowel_list.pop()
            else:
                # add the character to the string
                new_string += s[i]
        # return the new string
        return new_string
    
# with a two pointer approach
    


    
class Solution:
    def reverseVowels(self, s: str) -> str:
        # create a list of vowels
        vowels = ['a', 'e', 'i', 'o', 'u']
        l = list(s)
        i , j = 0 , len(l) - 1
        while i < j:
            if l[i].lower() in vowels and l[j].lower() in vowels:
                l[i] , l[j] = l[j] , l[i]
                i += 1
                j -= 1
            elif l[i].lower() in vowels:
                j -= 1
            elif l[j].lower() in vowels:
                i += 1
            else:
                i += 1
                j -= 1
        return ''.join(l)