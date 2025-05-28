class Sneakers:
    def __init__(self, brand, size, color, price, quantity, material, number_of_sales):
        self.brand = brand
        self.size = size
        self.color = color
        self.price = price
        self.quantity = quantity
        self.material = material
        self.number_of_sales = number_of_sales

    def __del__(self):
        print(f"Снікерси {self.brand} видалено з пам’яті.")

    def get_info(self):
        return (f"Бренд: {self.brand}, Розмір: {self.size}, Колір: {self.color}, "
                f"Ціна: {self.price} грн, Кількість: {self.quantity}, "
                f"Матеріал: {self.material}, Продано: {self.number_of_sales}")

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def get_number_of_sales(self):
        return self.number_of_sales


class SportShoesStore:
    def __init__(self):
        self.sneakers_list = []

    def add_sneakers(self, sneakers):
        self.sneakers_list.append(sneakers)

    def show_all(self):
        for sneaker in self.sneakers_list:
            print(sneaker.get_info())

    def sort_by_price(self):
        return sorted(self.sneakers_list, key=lambda s: s.get_price())

    def sort_by_quantity(self):
        return sorted(self.sneakers_list, key=lambda s: s.get_quantity(), reverse=True)

    def top_popular(self, top_n=3):
        sorted_by_sales = sorted(self.sneakers_list, key=lambda s: s.get_number_of_sales(), reverse=True)
        return sorted_by_sales[:top_n]


def main():
    store = SportShoesStore()

    # Додавання кросівок
    store.add_sneakers(Sneakers("Nike", 42, "чорні", 3500, 10, "сітка", 150))
    store.add_sneakers(Sneakers("Adidas", 43, "білі", 3000, 5, "шкіра", 180))
    store.add_sneakers(Sneakers("Puma", 41, "сині", 2800, 15, "замша", 90))
    store.add_sneakers(Sneakers("New Balance", 42, "сірі", 3200, 8, "текстиль", 120))

    print("\n--- Всі кросівки ---")
    store.show_all()

    print("\n--- Сортування за ціною ---")
    for s in store.sort_by_price():
        print(s.get_info())

    print("\n--- Сортування за кількістю ---")
    for s in store.sort_by_quantity():
        print(s.get_info())

    print("\n--- Топ популярних кросівок ---")
    for s in store.top_popular(3):
        print(s.get_info())


if __name__ == "__main__":
    main()
