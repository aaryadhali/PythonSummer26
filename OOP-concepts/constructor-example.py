import inspect

class car:
    def __init__(self):
        self.word = "dfdfdfd"
        print('fdfdf')

    #display_info()
print("Method object:", car.__init__)

try:
    print("\nSource code of __init__:\n")
    print(inspect.getsource(car.__init__))
except OSError:
    print("Source code not available.")

def display_info(self):
        """
        Displays the car's information.
        """
        print(f"Car: {self.word}")

    
if __name__ == "main":
    myCar = car()
    myCar.__init__
    print("Default values after creation:")
    myCar.display_info()