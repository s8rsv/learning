def change_price(products, name, new_price):
    if name in products:
        products[name] = new_price
        return 1
    return -1


products = {
    "mouse": 1500,
    "keyboard": 3000,
    "monitor": 12000
}

name = input("Введите товар: ").lower()
new_price = int(input("Введите новую цену: "))

result = change_price(products, name, new_price)

if result == 1:
    print("Цена успешно изменена!")
    print("Новая цена:", products[name])
else:
    print("Товар не найден")

print("Все товары:", products)