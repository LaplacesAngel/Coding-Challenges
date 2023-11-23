inv = {
    'Sword': 3,
    'Potion': 3
}

loot = {
    'Sword': 1,
    'Potion': 2,
    'Shield': 1
}

inv.update(loot)
print(type(inv))


print(inv)