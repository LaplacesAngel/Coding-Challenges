listofthings = [
    'belt',
    'shoes',
    'sword',
    'hammer',
    'shield',
    'christmas tongs'
]

#TODO move sword to the top of the list

index = listofthings.index('christmas tongs')
stuff = listofthings.pop(index)
listofthings.insert(0, stuff)

print(listofthings)