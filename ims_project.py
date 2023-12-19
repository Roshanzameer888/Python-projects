class InventoryManagementSystem:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name, quantity):
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if item_name in self.inventory:
            if self.inventory[item_name] >= quantity:
                self.inventory[item_name] -= quantity
                if self.inventory[item_name] == 0:
                    del self.inventory[item_name]
                print(f"{quantity} units of {item_name} removed from inventory.")
            else:
                print(f"Error: Not enough {item_name} in inventory.")
        else:
            print(f"Error: {item_name} not found in inventory.")

    def display_inventory(self):
        print("\nCurrent Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity} units")

# Example usage
if __name__ == "__main__":
    ims = InventoryManagementSystem()

    # Adding items to inventory
    ims.add_item("Bread", 100)
    ims.add_item("Milk", 50)
    ims.add_item("Eggs", 200)

    # Displaying initial inventory
    ims.display_inventory()

    # Removing items from inventory
    ims.remove_item("Bread", 20)
    ims.remove_item("Milk", 75)
    ims.remove_item("Cheese", 10)  # This item is not in inventory

    # Displaying updated inventory
    ims.display_inventory()
