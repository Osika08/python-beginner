data = list(range(6))
sqr = []
for x in data:
    value = x**2
    sqr.append(value)

    print(sqr)


word = "12345"
set = []
for char in word:
    s = int(char)

print(set)


product ={
    "id":1,
    "name":"iphone 16 pro max",
    "price":1599.99,
    "quantity":25,
    "is_available":True
}

# product["quantity"] = 9
# product.pop("quantity")

print(f"we have {product['quantity']} {product['name']} going for ${product["price"]} each currently available")
