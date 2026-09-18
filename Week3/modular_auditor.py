def get_valid_input():
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
            else:
                inventory = process_delivery(inventory, inventory_input)
        else:
            print("Invalid input! Please enter a number or 'quit' to exit.")
            reject_count += 1
    return inventory, reject_count

def process_delivery(current_total, new_value):
    current_total += int(new_value)
    return current_total

def calculate_tax(amount):
    tax_rate = 0.1
    return amount * tax_rate

def generate_report(inventory, reject_count):
    print("====== Delivery Report ======")
    print("Total Deliveries Processed:", inventory)
    print("Total Tax Amount:", calculate_tax(inventory))
    print("Number of Failed/Rejected Entries:", reject_count)

inventory, reject_count = get_valid_input()
generate_report(inventory, reject_count)