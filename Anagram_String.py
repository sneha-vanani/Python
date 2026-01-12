"""22. Write a function to check if a string is an anagram.
Compare two strings

Verify whether:

Both strings have the same length

Both strings have the same characters with the same frequency"""

# Old logic

# def anagram(s1,s2):
#     if len(s1) == len(s2):
#         for i in s1:
#             if i in s2:
#                 continue
#             else:
#                 return False
#         else:
#             return True

def anagram(s1,s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()


    if len(s1) != len(s2):
        return False
    
    return sorted(s1) == sorted(s2)


s1 = input('enter first string: ')
s2 = input('enter a string two compare it with first: ')

if anagram(s1,s2):
    print('anagram')
else:
    print('not anagram')