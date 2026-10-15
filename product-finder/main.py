products = {
    "mouse": 1500,
    "keyboard": 3000,
    "monitor": 12000
}

name = input("Введите название товара: ").lower()
def find_product(products, name):
    if name in products:
        return products[name]
    return None


result = find_product(products, name)
print(result)
print(products)

def change_price(products, name, new_price):
    if name in products:
        products[name] = new_price
        return 1
    return -1

name = input("Введите товар: ").lower()
new_price = int(input("Введите новую цену: "))

result = change_price(products, name, new_price)

if result == 1:
    print("Цена успешно изменена!")
    print("Новая цена:", products[name])
else:
    print("Товар не найден")

print("Все товары:", products)

def remove_product(products, name):
    if name in products:
        del products[name]
        return True
    return False

name = input("Введите товар, который хотите удалить: ").lower()

result = remove_product(products, name)

if result:
    print("Товар успешно удалён!")
else:
    print("Товар не найден")

print(" товары:", products)