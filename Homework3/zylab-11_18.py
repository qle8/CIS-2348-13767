# Name: Quang Le
# Student ID: 1768324 

user_input = input()

tokens = user_input.split()

nums = []
for token in tokens:
    nums.append(int(token))

for val in nums[:]:
    if val < 0:
        nums.remove(val)

nums.sort()
for num in nums:
    print(num, end=' ')
