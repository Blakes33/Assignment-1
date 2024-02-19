def read_product_data(file_name):
    products = []  # Initialize an empty list to store products
    
    # Open the file in read mode
    with open(file_name, 'r') as file:
        # Read each line in the file
        for line in file:
            # Split the line into attributes and strip any extra spaces
            attributes = line.strip().split(',')
            
            # Create a dictionary for the product
            product = {
                'ID': attributes[0].strip(),
                'Name': attributes[1].strip(),
                'Price': float(attributes[2].strip()),  # Convert price to float
                'Category': attributes[3].strip()
            }
            
            # Append the product dictionary to the products list
            products.append(product)
    
    return products

# Example usage:
file_name = "product_data.txt"
products = read_product_data(file_name)

# Print the products for verification
#for product in products:
    #print(product)

class ProductManager:
    def __init__(self, products):
        self.products = products
        
    def insert_product(self, product):
        self.products.append(product)
        print("Data: ", new_product, " Added Successfully.")
    
    def update_product(self, product_id, new_product):
        for i, product in enumerate(self.products):
            if product['ID'] == product_id:
                self.products[i] = new_product
                print("Product updated successfully")
                return True  # Product updated successfully
        return False  # Product with given ID not found
    
    def delete_product(self, product_id):
        for i, product in enumerate(self.products):
            if product['ID'] == product_id:
                del self.products[i]
                print("Product " +product_id+ " deleted successfully")
                return True  # Product deleted successfully
        return False  # Product with given ID not found
    
    def search_product(self, key, value):
        found_products = []
        for product in self.products:
            if product[key] == value:
                found_products.append(product)
        return found_products

# Example usage:
file_name = "product_data.txt"
products_data = read_product_data(file_name)
product_manager = ProductManager(products_data)

# Insert a new product
new_product = {'ID': '11573', 'Name': 'iPod', 'Price': 99.99, 'Category': 'Electronics'}
product_manager.insert_product(new_product)

# Update a product
updated_product = {'ID': '30631', 'Name': 'Headphones', 'Price': 122.99, 'Category': 'Electronics'}
product_manager.update_product('30631', updated_product)

# Delete a product
product_manager.delete_product('44574')

# Search for products by category
search_result = product_manager.search_product('Name', 'Headphones')
print("Search results for Headphones:")
for product in search_result:
    print(product)


import time

def bubble_sort_by_price(products):
    n = len(products)
    
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if products[j]['Price'] > products[j+1]['Price']:
                products[j], products[j+1] = products[j+1], products[j]

# First sort:
print("Products before sorting:")
for product in products_data:
    print(product)

start_time = time.time()  # Record the start time
bubble_sort_by_price(products_data)
end_time = time.time()  # Record the end time

print("\nProducts after sorting by price:")
for product in products_data:
    print(product)

total_time = end_time - start_time
print("\nTotal execution time: {:.6f} seconds".format(total_time))

# Re-sort:
print("Products before sorting:")
for product in products_data:
    print(product)

start_time = time.time()  # Record the start time
bubble_sort_by_price(products_data)
end_time = time.time()  # Record the end time

print("\nProducts after sorting by price:")
for product in products_data:
    print(product)

total_time = end_time - start_time
print("\nTotal execution time: {:.6f} seconds".format(total_time))

# Reverse sort:
def bubble_sort_by_price_desc(products):
    n = len(products)
    
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is less than the next element
            if products[j]['Price'] < products[j+1]['Price']:
                products[j], products[j+1] = products[j+1], products[j]

bubble_sort_by_price_desc(products_data)

print("Products before sorting:")
for product in products_data:
    print(product)

start_time = time.time()  # Record the start time
bubble_sort_by_price(products_data)
end_time = time.time()  # Record the end time

print("\nProducts after sorting by price:")
for product in products_data:
    print(product)

total_time = end_time - start_time
print("\nTotal execution time: {:.6f} seconds".format(total_time))