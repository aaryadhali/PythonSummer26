class Car: #class names should be capital
    
    def __init__(self, make, model, year, color): #self refers to the object
        self.make = make 
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("this {} is driving".format(self.model))
    
    def stop(self):
        print(f"this {self.model} is stopped")

if __name__ == "__main__":
    print("Testing the Car class directly!")
    test_car = Car("Chevy","Corvette", 2021, "blue")
    print(test_car.model)

"""If you click "Run" on car.py: 
Python sets __name__ to "__main__". 
The code inside the if block will run.

If you import car.py into main.py: 
Python sets __name__ to "car". 
The code inside the if block will be ignored.

It allows you to put testing code inside 
your class file without that testing code
accidentally running when you import the
class elsewhere."""