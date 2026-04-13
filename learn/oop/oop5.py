#Polymorphism

class Car:
    def __init__(self,brand,model):
        self.brand=brand   # here variable ke samne 2 underscore lagate hi ye private  ho jata hai
        self.model=model
        
    def get_brand(self):
        return self.brand
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
        
    def fuel_type(self):
        return "Electric Charge"

safari=Car("Tata","safari")
print(safari.fuel_type())

tesla=ElectricCar("Tesla","Model S","85kwh")
print(tesla.fuel_type())
    
    