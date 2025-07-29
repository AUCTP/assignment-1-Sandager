import random

# Some example items - feel free tho change them
items = ["Sandwich", "Butter Chicken", "Cake", "Pizza", "Pasta"]
prices = [65, 80, 50, 120, 90]
inventories = [100, 50, 100, 30, 60]

def main():
    print("Welcome to the Restaurant Sales Simulation!")
    num_customers = int(input("Enter the number of customers: "))
    
    sales = simulate_customers(num_customers)
    total_revenue = process_sales(sales)
    
    generate_report(total_revenue)


def simulate_customers(num_customers):
    sales = []
    for _ in range(num_customers):
        if random.random() < 0.5: 
            item_index = random.randint(0, len(items) - 1)
            if inventories[item_index] > 0:  
                inventories[item_index] -= 1  
                sales.append(item_index)  
    return sales

def process_sales(sales):
    total_revenue = 0
    for item_index in sales:
        total_revenue += prices[item_index]
    return total_revenue

def generate_report(total_revenue):
    print("Sales Report:")
    print(f"Total Revenue: ₹{total_revenue}")
    print("Remaining Inventory:")
    for i in range(len(items)):
        print(f"{items[i]}: {inventories[i]} remaining")

main()