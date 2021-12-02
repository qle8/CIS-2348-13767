# Name: Quang Le
# Student ID: 1768324



txt = input()
pldm = txt.replace(' ', '').lower()
revrs = pldm[::-1]
if pldm == revrs:
    print(txt, 'is a palindrome')

else:
    print(txt, 'is not a palindrome')
