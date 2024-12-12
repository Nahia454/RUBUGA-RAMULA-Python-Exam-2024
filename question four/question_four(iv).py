class Car:
    def __init__(self, brand, name, color):
        self.brand = brand
        self.name = name
        self.color = color
my_car = Car("Toyota", "Prado", "maroon")

# Print the attributes of the object
print("Brand:", my_car.brand)
print("Name:", my_car.name)
print("Color:", my_car.color)

