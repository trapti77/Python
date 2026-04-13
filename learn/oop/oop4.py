#Encapsulation

class Car:
    def __init__(self,brand,model):
        self.__brand=brand   # here variable ke samne 2 underscore lagate hi ye private  ho jata hai
        self.model=model
        
    def get_brand(self):
        return self.__brand

my_car=Car("Tata","Safari")

# print(my_car.__brand)
print(my_car.model)
print(my_car.get_brand())
