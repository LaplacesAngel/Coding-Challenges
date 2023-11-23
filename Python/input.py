# print(input("Name: ") or 'n/a')

# name  = input("Name: ") or 'n/a'

# othername = input("Name: ")

# print(name)

user_input = input("Name: ")
if user_input:
    name = user_input
else:
    name = 'N/A'

print(name)

#better way

name = input("Name: ") or 'N/A'
print(name)

#most efficient

print(input('name: ') or 'n/a')