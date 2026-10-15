products = {
    "mouse": 1500,
    "keyboard": 3000,
    "monitor": 12000
}

def find_product(products, name):
    if name in products:
        return products[name]
    return None

while True:
    print("1. Найти товар")
    print("2. Изменить цену")
    print("3. Удалить товар")
    print("4. Показать все товары")
    print("0. Выход")

    choice = input("Выберите действие: ")

    if choice == "0":
        print("Программа завершена")
        break

    elif choice == "1":
        name = input("Название товара: ").lower()
        price = find_product(products, name)

        if price is not None:
            print("Цена:", price)
        else:
            print("Товар не найден")
