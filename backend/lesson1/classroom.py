#  python -m venv venv 

# cop asoslari
# a = 6
# def add():
#   pass
# print(type(a))
# print(type{add()})

class Car:
    brand = "GM"

    def __init__(self, year, price, color):
        self.year = year
        self.price = price
        self.color = color
        self.is_engine_on = False

    def __str__(self):
        return f"{self.year}-yilgi mashina"

    def __repr__(self):
        return f"Car(year={self.year}, price={self.price}, color={self.color})"

    def start_car(self):
        if not self.is_engine_on:
            self.is_engine_on = True
            return "Car is successfully turned on!"
        return "Car is already on!"

    def drive(self):
        if self.is_engine_on:
            return "We are driving, look at the road!"
        return "You should start engine first!"


gentra = Car(year=2023, price=10000, color="Qora")
print(gentra.drive())
print(gentra.start_car())
print(gentra.start_car())
print(gentra.drive())

    
# list()
# print(repr(obj1))
# print(obj2.price)
# print(obj2.color)




