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

print("Все товары:", products)

while True:
    print("1. Найти товар")
    print("2. Выйти")

    choice = input("Выберите действие: ")

    if choice == "2":
        break
    else:
        def find_product(products, name, price):
        if name in products:
            products[name] = new_price
            return True
        return False
        

