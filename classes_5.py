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
        print(f"Кросівки {self.brand} видалено з пам’яті.")

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
        n = len(self.sneakers_list)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.sneakers_list[j].get_price() > self.sneakers_list[j + 1].get_price():
                    self.sneakers_list[j], self.sneakers_list[j + 1] = self.sneakers_list[j + 1], self.sneakers_list[j]
        return self.sneakers_list

    def sort_by_quantity(self):
        n = len(self.sneakers_list)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.sneakers_list[j].get_quantity() < self.sneakers_list[j + 1].get_quantity():
                    self.sneakers_list[j], self.sneakers_list[j + 1] = self.sneakers_list[j + 1], self.sneakers_list[j]
        return self.sneakers_list

    def top_popular(self, top_n=3):
        # Ручне сортування за number_of_sales
        n = len(self.sneakers_list)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.sneakers_list[j].get_number_of_sales() < self.sneakers_list[j + 1].get_number_of_sales():
                    self.sneakers_list[j], self.sneakers_list[j + 1] = self.sneakers_list[j + 1], self.sneakers_list[j]
        result = []
        count = 0
        for sneaker in self.sneakers_list:
            if count < top_n:
                result.append(sneaker)
                count += 1
        return result