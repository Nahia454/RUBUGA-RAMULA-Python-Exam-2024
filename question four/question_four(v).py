class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def describe(self):
        print(f"This car is a {self.year} {self.brand} {self.model}")

    def start_engine(self):
        print(f"The engine of the {self.year} {self.brand} {self.model} has started.")

my_car = Car("Toyota", "Prado", 2017)
my_car.start_engine()

