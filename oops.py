class Car:
    def __init__(self,brand,model):
       self.__brand= brand
       self.model = model
    def full(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
            return self.__brand + " !"
    
    def fuel_type(self):
        return "Petrol or Diesel" 
    

class ElectricalCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
         
    def full(self):
        return f"{self.brand} {self.model} {self.battery_size}" 
    def fuel_type(self):
        return "Electric charge"
    



my_car = Car("Toyota","Fourtuner")
#print(my_car.brand)
print(my_car.full())

my_car2 = Car("tata","harrier")
#print(my_car2.brand)

my_electriccar = ElectricalCar("Tesla","ev","30,000 mah")
#print(my_electriccar.full())
print(my_electriccar.get_brand())
print(my_car2.fuel_type())
print(my_electriccar.fuel_type())