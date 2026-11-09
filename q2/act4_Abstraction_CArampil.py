from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass


class TempSensor(Sensor):
    def get_reading(self, temperatura):
        return f"[Temperature Sensor] Reading: {temperatura}"

class PHSensor(Sensor):
    def get_reading(self, ph_level):
        return f"[pH Sensor] Reading: {ph_level}"

#for task 1-4
temperature1 = TempSensor()
ph_sensor1 = PHSensor()

#FOR TASK 5

my_sensor = Sensor()
print(my_sensor.get_reading("24.5°C"))  

print("--- Lab Inventory System ---")
print(ph_sensor1.get_reading("7.2 pH (Neutral)"))
print(temperature1.get_reading("24.5°C"))

