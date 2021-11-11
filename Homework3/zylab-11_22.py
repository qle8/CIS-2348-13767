# Name: Quang Le
# Student ID: 1768324 

user_input = input()

tokens = user_input.split()

for token in tokens:
    vale = tokens.count(token)
    print("{} {}".format(token, vale))

