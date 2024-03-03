import random
import csv
from faker import Faker

fake = Faker()

# Main dict
category_products = {
    'Groceries': ["Rice", "Beans", "Pasta", "Bread"],
    'Dairy': ["Milk", "Eggs", "Cheese", "Yogurt", "Butter"],
    'Health & Beauty': ["Shampoo", "Soap", "Toothpaste"],
    'Cleaning': ["Detergent", "Disinfectant", "Bleach"],
    'Beverages': ["Water", "Soda", "Juice", "Coffee", "Tea"]
}

# Map product + ID
product_ids = {}
id_counter = {}

with open('product_data2.csv', 'w', newline='') as csvfile:
    fieldnames = ['Product ID', 'Product Name', 'Category', 'Unit Price', 'Available Stock', 'Expiry Date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(1, 5001):

        #  Chose random category
        category = random.choice(list(category_products.keys()))

        # Choses random products from the category above
        product_name = random.choice(category_products[category])
        unit_price = round(random.uniform(1, 20), 2)
        available_stock = random.randint(10, 500)
        expiry_date = fake.date_this_year(after_today=True, before_today=False) if random.random() < 0.8 else '-'
        
        # Generates product ID
        product_id = f"{category[:2].upper()}{product_name[:2].upper()}"
        if product_id not in id_counter:
            id_counter[product_id] = 1
        else:
            id_counter[product_id] += 1
        product_id += f"{id_counter[product_id]:02}"
        
        print(f'Generating data for product {i}: {product_id}, {product_name}, {category}, ${unit_price}, {available_stock}, {expiry_date}')
        
        writer.writerow({
            'Product ID': product_id,  # ID mapped
            'Product Name': product_name,
            'Category': category,
            'Unit Price': unit_price,
            'Available Stock': available_stock,
            'Expiry Date': expiry_date
        })

print("Data generation completed.")
