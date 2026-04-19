#static method

class Car:
    total_car=0
    def __init__(self,brand,model):
        self.brand=brand   # here variable ke samne 2 underscore lagate hi ye private  ho jata hai
        self.model=model
        Car.total_car+=1
        
        
    def get_brand(self):
        return self.brand
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_desc():
        return "Cars are means of transport"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
        
    def fuel_type(self):
        return "Electric Charge"

safari=Car("Tata","safari")
# print(safari.general_desc())

tesla=ElectricCar("Tesla","Model S","85kwh")
# print(tesla.fuel_type())

print(Car.general_desc()) # static property only accessibal by class not by its object 

# as static property not accessible by object there is no need self because self is used to link class with its object
    
    
