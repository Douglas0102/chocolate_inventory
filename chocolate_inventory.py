import json

def sort_products(products, sort_key, ascending=True):
    sorted_products = sorted(products, key=lambda x: x[sort_key], reverse=not ascending)
    return sorted_products

with open('products_inventory.json', 'r') as file:
    products = json.load(file)

sort_key = "name"
ascending = True

sorted_products = sort_products(products, sort_key, ascending)
for product in sorted_products:
    print(product)
