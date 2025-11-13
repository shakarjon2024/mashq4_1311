class Car:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
        self.__speed = 0


    def accelerate(self, amount):
        if amount > 0:
            self.__speed += amount
            if self.__speed > 250:
                self.__speed = 250
            print(f" {self.marka} {self.model} tezlashdi. Hozirgi tezlik: {self.__speed} km/h")
        else:
            print("Tezlik oshirish miqdori musbat bo‘lishi kerak!")


    def brake(self, amount):
        if amount > 0:
            self.__speed -= amount
            if self.__speed < 0:
                self.__speed = 0
            print(f" {self.marka} {self.model} sekinlashdi. Hozirgi tezlik: {self.__speed} km/h")
        else:
            print(" Tormoz miqdori musbat bo‘lishi kerak!")


    def _get_speed(self, system):
        if isinstance(system, CarControlSystem):
            return self.__speed
        else:
            return " Sizga tezlikni ko‘rish huquqi yo‘q!"


class CarControlSystem:
    def __init__(self, system_name):
        self.system_name = system_name


    def monitor_speed(self, car):
        speed = car._get_speed(self)
        if isinstance(speed, (int, float)):
            print(f" {car.marka} {car.model} tezligi: {speed} km/h")
            if speed > 200:
                print(" OGОHLANTIRISH! Tezlik xavfli darajada yuqori!")
        else:
            print(speed)



car1 = Car("Tesla", "Model S")
control_system = CarControlSystem("AvtoControl V1.0")


car1.accelerate(80)
car1.accelerate(90)


control_system.monitor_speed(car1)


car1.accelerate(50)
control_system.monitor_speed(car1)


car1.brake(150)
control_system.monitor_speed(car1)
