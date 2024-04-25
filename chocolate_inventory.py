def sort_products(products, sort_key, ascending=True):

    sorted_products = sorted(products, key=lambda x: x[sort_key], reverse=not ascending)
    return sorted_products

products = [
    {"name": "Hershey's", "price": 3.50, "stock": 100},
    {"name": "Cadbury", "price": 2.99, "stock": 80},
    {"name": "Lindt", "price": 4.25, "stock": 50},
    {"name": "Ghirardelli", "price": 5.75, "stock": 60},
    {"name": "Ferrero Rocher", "price": 8.99, "stock": 30},
    {"name": "Toblerone", "price": 3.75, "stock": 70},
    {"name": "Godiva", "price": 6.50, "stock": 40},
    {"name": "Nestlé", "price": 2.25, "stock": 90},
    {"name": "M&M's", "price": 1.99, "stock": 120},
    {"name": "Ritter Sport", "price": 2.50, "stock": 55}
]

sort_key = "name"
ascending = False

sorted_products = sort_products(products, sort_key, ascending)
for product in sorted_products:
    print(product)
