products = {
    "mouse": 1400,
    "microphone": 3000,
    "keyboard": 2000
}
name = input("Введите название товара: ").lower()
if name in products:
    print(products[name])

else:
    print("Товар не найден")

def change_price(products, name, new_price):
    if name in products:
        products[name] = new_price
        return True
    return False


def add_product(products, new_name, price):
    if new_name in products:
        return False

    products[new_name] = price
    return True
new_name = input("Введите новый товар: ").lower()
price = int(input("Введите цену нового товара: "))

result = add_product(products, new_name, price)

print("Результат:", result)
print("Все товары:", products)