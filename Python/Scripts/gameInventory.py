#this program is an inventory for a game

def displayInventory(inventory):#takes a dictionary and prints it "value" "key"
    print('Inventory')
    count = 0
    for item, amount in inventory.items():
        print(str(amount) + ' ' + item)
        count += amount
    print('Total number of items: ' + str(count))

def addToInventory(inventory, addedItems):
    for newItem in addedItems:
        inventory.setdefault(newItem, 0)
        inventory[newItem] = inventory[newItem] + 1
    return inventory


myBackpack = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 1000}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
displayInventory(myBackpack)
addToInventory(myBackpack,dragonLoot)
displayInventory(myBackpack)