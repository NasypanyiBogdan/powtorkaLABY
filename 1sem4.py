class Printer:
    def __init__(self, brand="Unknown", price=0, speed=0, name="Unknown", pages_printed=0, status="Idle"):
        self.__brand = brand             
        self.__price = price             
        self.__speed = speed             
        self.__name = name               
        self.pages_printed = pages_printed  
        self.status = status               

    def get_brand(self):
        return self.__brand

    def get_price(self):
        return self.__price

    def get_speed(self):
        return self.__speed

    def get_name(self):
        return self.__name

    def set_brand(self, brand):
        self.__brand = brand

    def set_price(self, price):
        self.__price = price

    def set_speed(self, speed):
        self.__speed = speed

    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return (f"Printer: {self.__name}, Brand: {self.__brand}, Price: {self.__price} грн, "
                f"Speed: {self.__speed} л/хв, Pages Printed: {self.pages_printed}, Status: {self.status}")

    def __repr__(self):
        return (f"Printer(name='{self.__name}', brand='{self.__brand}', price={self.__price}, "
                f"speed={self.__speed}, pages_printed={self.pages_printed}, status='{self.status}')")

    def __del__(self):
        print(f"Printer '{self.__name}' (brand: {self.__brand}) has been deleted.")


def main():
    printer1 = Printer("Canon", 3300, 30, "LBP-3116", 1200, "Ready")
    printer2 = Printer("LG", 5200, 48, "V-30Super", 800, "Printing")
    printer3 = Printer("Xiaomi", 1999, 36, "快速說明", 300, "Idle")

    printers = [printer1, printer2, printer3]

    for i, printer in enumerate(printers, start=1):
        print(f"\nPrinter {i}:")
        print("Brand:", printer.get_brand())
        print("Price:", printer.get_price(), "грн")
        print("Speed:", printer.get_speed(), "листків/хв")
        print("Model:", printer.get_name())
        print("Pages Printed:", printer.pages_printed)
        print("Status:", printer.status)
        print("Full description:", printer)

main()
