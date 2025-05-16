product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
class Product:
    def __init__(self,product_name = "", product_code = 0):
        self.product_name = product_name
        self.product_code = product_code

products = []
for i in range(2):
    products.append(Product("codetree", 50))

products[1].product_name = product_name
products[1].product_code = product_code

print(f"product {products[0].product_code} is {products[0].product_name}")
print(f"product {products[1].product_code} is {products[1].product_name}")