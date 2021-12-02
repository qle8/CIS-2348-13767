# Name: Quang Le
# Student ID: 1768324


# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    try:
        age = int(parts[1]) + 1
        print('{} {}'.format(name, age))
    except ValueError as excpt:
        print('{} 0'.format(name))

    parts = input().split()
    name = parts[0]
