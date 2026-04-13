#Inheritance

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_Size):
        super().__init__(brand,model)
        self.battery_Size=battery_Size
        
        
my_tesla=ElectricCar("Tesla","Model S","85Kwh")
print(my_tesla.model)
print(my_tesla.brand)
print(my_tesla.battery_Size)
    
        
