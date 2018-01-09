# Fantasy Game Inventory
# Automate The Boring Stuff Ch.5
# Oscar Padilla


# Outputs inventory items and quantities
def display_inventory(bag):
    total = 0
    print("Inventory:")
    for k, v in bag.items():
        print(str(v) + " " + str(k))
        total += v
    print("Total number of items: %d" % total)


# Add items and update inventory
def add_inventory(bag, addedItems):
    for item in addedItems:
        new = True
        for k, v in bag.items():
            if item == str(k):
                bag[k] = v + 1
                new = False
        if new:
            bag[item] = 1
    return bag


inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']  # Added items

inventory = add_inventory(inventory, loot)
display_inventory(inventory)
