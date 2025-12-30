#Management system
mainMenu = (
    "1.Add Item", 
    "2.View Inventory", 
    "3.Update Item", 
    "4.Remove Item", 
    "5.Exit"
    )
inventory = dict()

#implement error handling
try:
    selectedOption = int(input("Select an option: > "))
except ValueError:
    print("Please select menu 1-5")
    continue


def printMenu(menuItems):
    for menu in menuItems:
        print(menu)

def askYesNo(prompt): #use for let user want to add new item or not
    answer = input(prompt).strip().lower()  
    return answer in ("y","yes") 

def addItem(): 
    print("Add item")
    name = input("Item Name: ").strip().lower()
    if not name:
        print("Item Name cannot be empty")
        return
    key = name.lower()
    if key in inventory: 
        old = inventory[key] 
        print("Item already exist.")
        print(f"- Current item details: Item Name: {old['name']} | Quantity: {old['quantity']} | Price: {old['price']}")
        replace = askYesNo("Replace this Item? (y/n):")
        if not replace: # if user say no -> false -> user want to add new item
            create_new = askYesNo("Create a new item with number incrementation? (y/n)")
            if not create_new: #if user say yes that mean this is not gonna happen
                print("Operation Cancelled...")
                return
            base = name
            counter = 2 # will start at 2 because already found the 1st one
            new_name = f"{base} - ({counter})"
            while new_name.lower() in inventory: #check again if have same name
                counter += 1
                new_name = f"{base} - ({counter})"
            print(f"Suggested Item name: {new_name}")
            use_suggested = askYesNo("Use the suggested Item name? (y/n):")
            if use_suggested:
                name = new_name
                key = name.lower()
            else:
                name = input("Enter a new name: ").strip()
                if not name:
                    print("Name cannot be empty")
                    return
                key = name.lower()
                if key in inventory:
                    print("Item already exist.")
                    return

    quantity = int(input("Quantity: ").strip())
    price = float(input("Price: ").strip())            
    inventory[key] = {"name": name , "quantity": quantity ,"price": price}
    print(f"{name} added successfully!")

def viewInventory():
    print("Current Inventory:")
    for item in inventory.values():
        for key,val in item.items():
            print(f"{key}:{val}")
        print("*"*10)

def updateItem():
    print("Search Contact". center(50, "*"))
    query = input("Enter item name to update: ").strip()
    if not query:
        print("Item name cannot be empty.")
        return
    key = query.lower()
    if key in inventory:
        foundItem = inventory[key]
        print(f"Item Found: Name {foundItem['name']} | Quantity({foundItem['quantity']}) | Price({foundItem['price']})")
    else:
        print("No Item found.")

        #then user can edit
    
def removeItem():
    print("Remove Item".center(50,"*"))
    query = input("Enter item name to remove: ").strip()
    if not query:
        print("Item name cannot be empty.")
        return
    key = query.lower()
    if key in inventory:
        removed = inventory.pop(key)
        print(f"{'query'} is removed...")
    else: 
        print("No Item found.")

while(selectedOption != 5):
    printMenu(mainMenu)
    selectedOption = int(input("Select an option: > ")) 
    if(selectedOption not in range(1,6)): 
        print("Please select option 1-5")
        continue
    if selectedOption == 1:
        addItem()
    if selectedOption == 2:
        viewInventory()
    if selectedOption == 3:
        updateItem()
    if selectedOption == 4:
        removeItem()
print("Exiting system. Goodbye!")