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

# This line acts as a gatekeeper. 
# It determines whether your Python file is 
# being run directly by you,# or if it is
# being imported by another file.


if __name__ == "main": 
    myCar = car()
    myCar.__init__
    print("Default values after creation:")
    myCar.display_info()