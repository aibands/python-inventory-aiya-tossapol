#Groceries Inventory Management system
mainMenu = (
    "1.Add Item", 
    "2.View Inventory", 
    "3.Update Item", 
    "4.Remove Item", 
    "5.Exit"
    )

inventory = dict()
item_id = set() 
categories = ["Produce", "Beverages", "Snacks"]

#product class
class product:
    def __init__(self, id, name, quantity, price, brand):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.brand = brand
    
    def showProduct(self):
        print(
            f"Item Id: {self.id} | "
            f"Item Name: {self.name} | "
            f"Brand: {self.brand} | "
            f"Quantity: {self.quantity} | "
            f"Price: ${self.price:.2f}"
        )

#for update #no need for brand because can't change
    def update(self, name=None, quantity=None, price=None):
        if name is not None:
            self.name = name
        if quantity is not None:
            self.quantity = quantity
        if price is not None:
            self.price = price

#expiration date sub class
class PerishableProduct(product):
    def __init__(self, id, name, quantity, price, brand, expiration_date):
        super().__init__(id, name, quantity, price, brand)
        self.expiration_date = expiration_date

#file
def saveInventory():
    with open("inventory.txt", "w") as file:
        for product in inventory.values():
            file.write(
                file.write(f"{product.id},{product.name},{product.brand},{product.quantity},{product.price}")
            )

def readInventory():
    try:
        with open("inventory.txt", "r") as file:
            for line in file:
                id, name, quantity, price, brand = line.strip().split(",")
                item = product(int(id), name, (brand), int(quantity), float(price))
                inventory[name.lower()] = item
                item_id.add(int(id))
    except FileNotFoundError:
        print("File not found.")
        pass
    

def printMenu(menuItems):
    print("Welcome to the Inventory Management System!")
    print("=" * 50)
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
        print(f"- Current item details: Item Name: {old['id']} | Item Name: {old['name']} | Brand: {old['brand']} | Quantity: {old['quantity']} | Price: {old['price']}")

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

    brand = input("Brand: ").strip().lower()
    quantity = int(input("Quantity: ").strip())
    price = float(input("Price: ").strip())            
    inventory[key] = product(id=len(item_id)+1, name=name, quantity=quantity, price=price, brand=brand)
    item_id.add(len(item_id)+1)

def viewInventory():
    print("Inventory". center(50, "*"))
    if not inventory:
        print("Inventory is empty.")
        return

    print("Current Inventory:")
    for item in inventory.values():
        for key,val in item.items():
            print(f"{key}:{val}")
        print("*"*10)


def updateItem():
    print("Update Item". center(50, "*"))
    query = input("Enter item name to update: ").strip()
    if not query:
        print("Item name cannot be empty.")
        return

    key = query.lower()
    if key in inventory:
        foundItem = inventory[key]
        print(f"Item Found: Name: {foundItem['name']} | Brand: {foundItem['brand']} |Quantity: {foundItem['quantity']} | Price: {foundItem['price']}")
    else:
        print("No Item found.")

    print("Press ENTER to keep current value")
    new_name = input("New name: ").strip()
    new_qty = input("New quantity: ").strip()
    new_price = input("New price: ").strip()

    foundItem = inventory[key]
    foundItem.update(
        name=new_name if new_name else None,
        quantity=int(new_qty) if new_qty else None,
        price=float(new_price) if new_price else None
    )
    #replace old one
    if new_name:
        inventory[new_name.lower()] = inventory.pop(key)

    print("Inventory updated successfully!")

def removeItem():
    print("Remove Item".center(50,"*"))
    query = input("Enter item name to remove: ").strip()
    if not query:
        print("Item name cannot be empty.")
        return
    key = query.lower()
    if key in inventory:
        removed = inventory.pop(key)
        print(f"{query} is removed...")
    else: 
        print("No Item found.")

selectedOption = 0
while(selectedOption != 5):
    printMenu(mainMenu)
    try:
        selectedOption = int(input("Select an option: > "))
    except ValueError:
        print("Please select option 1-5")
        continue

    if selectedOption == 1:
        addItem()
    elif selectedOption == 2:
        viewInventory()
    elif selectedOption == 3:
        updateItem()
    elif selectedOption == 4:
        removeItem()
    elif selectedOption == 5:
        saveInventory()
    print("Saving inventory to file...")
    print("Exiting system. Goodbye!")