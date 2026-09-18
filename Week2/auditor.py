inventory = 0
reject_count = 0
while True:
    inventory_input = input("Enter stock quantity: ")
    if inventory_input == "quit":
        break
    elif inventory_input.isdigit():
        if inventory + int(inventory_input) > 500:
                print("Inventory limit exceeded!")
                reject_count += 1
                break
        else:
            inventory += int(inventory_input)
    else:
        print("Invalid input! Please enter a number or 'quit' to exit.")
        reject_count += 1

print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", reject_count)