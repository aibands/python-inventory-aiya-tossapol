# Groceries Inventory Management System
This project is part of the **Empowering the Web with Python and Django** subject.  
It is a simple Python-based inventory management system for grocery items, including **Produce, Beverages, and Snacks**.  
The system allows you to **add, view, update, and remove grocery products** while keeping track of their details, such as name, brand, quantity, price, and category.

---

## How to Run
1. Clone or download this repository.
2. Open a terminal and navigate to the project folder.
3. Run the program:
    ```bash
    python3 aiya_coursework1.py
4. Follow the on-screen menu in the management system.

## Features implemented
- Add new items to inventory
- View current inventory
- Update existing items 
- Remove items from inventory
- Save inventory to a text file (inventory.txt)
- Handles duplicate items and name conflicts
- Simple category selection from a predefined list (Produce, Beverages, Snacks)

## Limitations
- Categories are limited to the predefined list. 
- Inventory is saved in a simple text file, not a database.
- No search/filter functionality by brand, category, or price range.
- Error handling is basic; unexpected input may cause program to exit.
- Perishable product subclass exists but expiration dates are not fully implemented in main workflow.