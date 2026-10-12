products = {
    "mouse": 1500,
    "keyboard": 3000,
    "monitor": 12000
}

name = input("Введите название товара: ").lower()

if name in products:
    print(products[name])
else:
    print("Товар не найден")
    