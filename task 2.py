import tkinter as tk
import os

def authenticate():
    """Authenticate the user."""
    if username_entry.get() == "admin" and password_entry.get() == "2004":
        login_frame.pack_forget()
        main_frame.pack()
    else:
        auth_label.config(text="Invalid credentials!", fg="red")

def modify_inventory(action):
    """Add, update, or remove inventory items."""
    item_name = item_name_entry.get().strip()
    item_qty = item_qty_entry.get().strip()
    item_price = item_price_entry.get().strip()

    if not item_name:
        output_label.config(text="Item name required!", fg="red")
        return

    inventory = {}
    if os.path.exists('inventory.txt'):
        with open('inventory.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    inventory[parts[0]] = parts  # {name: [name, qty, price]}

    if action in ["add", "update"]:
        if not (item_qty.isdigit() and item_price.replace('.', '', 1).isdigit()):
            output_label.config(text="Enter valid quantity and price!", fg="red")
            return
        inventory[item_name] = [item_name, str(int(item_qty)), str(float(item_price))]

    elif action == "remove":
        if item_name in inventory:
            del inventory[item_name]
        else:
            output_label.config(text="Item not found!", fg="red")
            return

    with open('inventory.txt', 'w') as file:
        for item in inventory.values():
            file.write(",".join(item) + "\n")

    output_label.config(text=f"{action.capitalize()} successful!", fg="green")
    clear_entries()

def search_inventory():
    """Search for an item in inventory."""
    item_name = item_name_entry.get().strip()
    if not os.path.exists('inventory.txt'):
        output_label.config(text="Inventory file not found!", fg="red")
        return

    with open('inventory.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 3 and parts[0] == item_name:
                output_label.config(text=f"Found: {parts[0]} - Qty: {parts[1]}, Price: {parts[2]}", fg="blue")
                return
    output_label.config(text="Item not found!", fg="red")

def generate_inventory():
    """Display all inventory items."""
    if not os.path.exists('inventory.txt') or os.stat('inventory.txt').st_size == 0:
        output_label.config(text="Inventory is empty!", fg="black")
        return

    with open('inventory.txt', 'r') as file:
        data = file.read()
        output_label.config(text=f"Inventory Data:\n{data}", fg="black")

def clear_entries():
    """Clear input fields."""
    item_name_entry.delete(0, tk.END)
    item_qty_entry.delete(0, tk.END)
    item_price_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Inventory Manager")

# Login UI
login_frame = tk.Frame(root)
login_frame.pack()
tk.Label(login_frame, text="Username:").grid(row=0, column=0)
username_entry = tk.Entry(login_frame); username_entry.grid(row=0, column=1)
tk.Label(login_frame, text="Password:").grid(row=1, column=0)
password_entry = tk.Entry(login_frame, show="*"); password_entry.grid(row=1, column=1)
auth_label = tk.Label(login_frame); auth_label.grid(row=2, columnspan=2)
tk.Button(login_frame, text="Login", command=authenticate).grid(row=3, columnspan=2)

# Inventory UI
main_frame = tk.Frame(root)

tk.Label(main_frame, text="Item Name:").grid(row=0, column=0)
item_name_entry = tk.Entry(main_frame)
item_name_entry.grid(row=0, column=1)

tk.Label(main_frame, text="Quantity:").grid(row=1, column=0)
item_qty_entry = tk.Entry(main_frame)
item_qty_entry.grid(row=1, column=1)

tk.Label(main_frame, text="Price:").grid(row=2, column=0)
item_price_entry = tk.Entry(main_frame)
item_price_entry.grid(row=2, column=1)

tk.Button(main_frame, text="Add", command=lambda: modify_inventory("add")).grid(row=3, column=0)
tk.Button(main_frame, text="Update", command=lambda: modify_inventory("update")).grid(row=3, column=1)
tk.Button(main_frame, text="Remove", command=lambda: modify_inventory("remove")).grid(row=3, column=2)
tk.Button(main_frame, text="Search", command=search_inventory).grid(row=4, column=0)
tk.Button(main_frame, text="Generate Inventory", command=generate_inventory).grid(row=4, column=1)

output_label = tk.Label(main_frame, text="", fg="black")
output_label.grid(row=5, columnspan=3)

root.mainloop()
