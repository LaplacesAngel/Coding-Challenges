oglist = ['a', 'b', 'a', 'c', 'a', 'd']

#TODO remove duplicates while retaining list order

newlist = []
for letter in oglist:
    if newlist.__contains__(letter):
        continue
    newlist.append(letter)

otherNewList= []
for letter in oglist:
    if letter not in otherNewList:
        otherNewList.append(letter)


setlist = list(set(oglist))

for letter in setlist:
    print(letter)


print(newlist)
print(setlist)
print(otherNewList)