"""22. Write a function to check if a string is an anagram.
Compare two strings

Verify whether:

Both strings have the same length

Both strings have the same characters with the same frequency"""

def anagram(s1,s2):
    if len(s1) == len(s2):
        for i in s1:
            if i in s2:
                continue
            else:
                return False
        else:
            return True


s1 = input('enter first string: ')
s2 = input('enter a string two compare it with first: ')

if anagram(s1,s2):
    print('anagram')
else:
    print('not anagram')