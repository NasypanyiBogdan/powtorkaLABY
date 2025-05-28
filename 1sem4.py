class Printer:

    def __init__(self, brand="Unknown", price=0, speed=0, name="Unknown"):
        self.__brand = brand
        self.__price = price
        self.__speed = speed
        self.name = name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_speed(self):
        return self.__speed
    def set_speed(self, speed):
        self.__speed = speed

    def get_name(self):
        return self.name

    def set_name (self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"{self.name}"

    def __del__(self):
        print(f"Printer {self.get_brand} {self.get_name()} # deleted")

def main():
    kanon = Printer("kanon", 3300, 30, "lbp-3116")
    print(f"Brand {kanon.get_brand()}, price = {kanon.get_price()} грн, printspeed = {kanon.get_speed()} листків/хв, model of the printer {kanon.get_name()}")
    LG = Printer("LG", 5200, 48, "v-30super")
    print(f"Brand {LG.get_brand()}, price = {LG.get_price()} грн, printspeed = {LG.get_speed()} листків/хв, model of the printer {LG.get_name()}")
    Xiaomi = Printer("Xiaomi", 1999, 36, "快速說明")
    print(f"Brand {Xiaomi.get_brand()}, price = {Xiaomi.get_price()} грн, printspeed = {Xiaomi.get_speed()} листків/хв, model of the printer {Xiaomi.get_name()}")

main()