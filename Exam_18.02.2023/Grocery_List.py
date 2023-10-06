def shop_from_grocery_list(budget, products, *args):
    purchased_product = []
    for el in args:
        product = el[0]
        price = float(el[1])
        if product in products and product not in purchased_product and budget >= price:
            purchased_product.append(product)
            products.remove(product)
            budget -= price
        elif budget < price:
            break

    if products:
        return f"You did not buy all the products. Missing products: {', '.join(products)}."
    else:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."

print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))