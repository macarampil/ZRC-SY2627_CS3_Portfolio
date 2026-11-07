#1. Answer the following questions:
#a. What is duck typing, as explained in the video?
# - Based on the video, duck typing simply means that if it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck. This means that an object's suitability for use is determined by the presence of certain methods/attributes, rather than the actual type of the object.
#b. What did the Car class need to have so it could work inside the same loop as Dog and
#Cat, even if it does not inherit from the Animal class?
# - The Car class needs to have the same method of the Dog and Cat classes that is speak() method. This allows the Car class to be used in the same loop as Dog and Cat, demonstrating polymorphism through duck typing.




#2. Create the Python code that:
#a. Creates three classes: Car, Boat, and Drone with a method move().
#move() in the Car class prints "The car drives on the road."
#move() in the Boat class prints "The boat sails on water."
#move() in the Drone class prints "The drone flies in the sky."
#b. Has a function named start_trip(vehicle), with a parameter vehicle, that simply calls the
#move() method: vehicle.move().
#c. Creates one object of each class.
#d. Calls the start_trip() method for each object.
#3. How does the code in 2.2 demonstrate polymorphism?
# - The code demonstrates polymorphism because the start_trip() function can accept different types of objects as long as they have a move() method, regardless of their class. This allows different objects (Car, Boat, and Drone) to be treated uniformly through the same interface, demonstrating polymorphism through duck typing.

class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")    


def start_trip(vehicle):
    vehicle.move()

car = Car()
boat = Boat()
drone = Drone()

start_trip(car)
start_trip(boat)
start_trip(drone)   