from classes_5 import Sneakers, SportShoesStore

def main():
    store = SportShoesStore()

    store.add_sneakers(Sneakers("Nike", 42, "чорні", 3500, 10, "сітка", 150))
    store.add_sneakers(Sneakers("Adidas", 43, "білі", 3000, 5, "шкіра", 180))
    store.add_sneakers(Sneakers("Puma", 41, "сині", 2800, 15, "замша", 90))
    store.add_sneakers(Sneakers("New Balance", 42, "сірі", 3200, 8, "текстиль", 120))

    print("\nВсі кросівки")
    store.show_all()

    print("\nСортування за ціною")
    sorted_by_price = store.sort_by_price()
    for s in sorted_by_price:
        print(s.get_info())

    print("\nСортування за кількістю")
    sorted_by_quantity = store.sort_by_quantity()
    for s in sorted_by_quantity:
        print(s.get_info())

    print("\nТоп популярних кросівок")
    top_popular = store.top_popular(3)
    for s in top_popular:
        print(s.get_info())


if __name__ == "__main__":
    main()