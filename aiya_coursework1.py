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
    def __init__(self, id, name, quantity, price, brand, category=None):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.brand = brand
        self.category = category
    
    def showProduct(self):
        print(
            f"Item Id: {self.id} | "
            f"Item Name: {self.name} | "
            f"Brand: {self.brand} | "
            f"Category: {self.category} | "
            f"Quantity: {self.quantity} | "
            f"Price: ${self.price:.2f}"
        )

#for update #no need for brand because can't change
    def update(self, name=None, category=None, quantity=None, price=None):
        if name is not None:
            self.name = name
        if category is not None:
            self.category = category
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
            file.write(f"{product.id},{product.name},{product.brand},{product.category},{product.quantity},{product.price}")

def readInventory():
    try:
        with open("inventory.txt", "r") as file:
            for line in file:
                id, name, category, quantity, price, brand = line.strip().split(",")
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
        print(
            f"- Current item details: ID: {old.id} | "
            f"Name: {old.name} | "
            f"Brand: {old.brand} | "
            f"Category: {old.category} | "
            f"Quantity: {old.quantity} | "
            f"Price: ${old.price:.2f}"
        )

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
    #add categories
    category = input(f"Select Categories({', '.join(categories)}): ").strip()
    if category not in categories:
        print("category not found, defaulting to none.")

    print(f"'{name}' added successfully!")


def viewInventory():
    print("Inventory". center(50, "*"))
    if not inventory:
        print("Inventory is empty.")
        return

    print("Current Inventory:")
    for item in inventory.values():
        print(
            f"ID: {item.id} | Name: {item.name} | Brand: {item.brand} | Category: {item.category} | Quantity: {item.quantity} | Price: ${item.price:.2f}"
        )


def updateItem():
    print("Update Item". center(50, "*"))
    query = input("Enter item name to update: ").strip()
    if not query:
        print("Item name cannot be empty.")
        return

    key = query.lower()
    if key not in inventory:
        print("No Item found.")
        return
    
    foundItem = inventory[key]
    print(
        f"Item Found Name: ID: {foundItem.id} | "
        f"Name: {foundItem.name} | "
        f"Brand: {foundItem.brand} | "
        f"Category: {foundItem.category} | "
        f"Quantity: {foundItem.quantity} | "
        f"Price: ${foundItem.price:.2f}"
        )

    print("Press ENTER to keep current value")
    new_name = input("New name: ").strip()
    new_qty = input("New quantity: ").strip()
    new_price = input("New price: ").strip()

    #quantity
    if new_qty:
        if new_qty.isdigit():
            new_qty = int(new_qty)
        else:
            print("Invalid quantity.")
            new_qty = None
    else:
        new_qty = None #keep old qty

    #price
    if new_price:
        try:
            new_price = float(new_price)
        except ValueError:
            print("Invalid price.")
            new_price = None
    else:
        new_price = None #keep old price

    foundItem.update(
        name=new_name if new_name else None,
        quantity=new_qty,
        price=new_price
    )

    #name
    if new_name:
        inventory[new_name.lower()] = inventory.pop(key)

    print("Inventory updated successfully!")

    #categories
    # Category
    new_category = input(f"New category ({', '.join(categories)}): ").strip()
    if new_category and new_category not in categories:
        print("Invalid category. Keeping old category.")
        new_category = None
    elif not new_category:
        new_category = None

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
        break
else:
    print("Please select option 1-5")
