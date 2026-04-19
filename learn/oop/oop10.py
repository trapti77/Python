# multiple inheritance
class Car:
    total_car=0
    def __init__(self,brand,model):
        self.brand=brand   
        self.__model=model
        Car.total_car+=1
        
        
    def get_brand(self):
        return self.brand
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_desc():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model
        
    
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
        
    def fuel_type(self):
        return "Electric Charge"


safari=Car("Tata","safari")
electricCar=ElectricCar("Tesla","Model S","85kwh")

class Battery:
    def batter_info(self):
        return "This is battery"

class Engine:
    def engine_info(self):
        return "this is engine"

class ElectricCarTwo(Battery,Engine,Car): #inherit three class
    pass


my_new_tesla=ElectricCarTwo("Telsa","Model S")

print(my_new_tesla.batter_info())
print(my_new_tesla.engine_info())
