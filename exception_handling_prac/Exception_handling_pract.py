"""exception = an event that interrupts the flow of 
            a program"""

#NameError
try:
    print(x/0)
except NameError:
    print("Define the variable")

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

#ZeroDivisionError
try:
    x=2
    print(x/0)
except ZeroDivisionError:
    print("Do not divide by 0")
finally:
   print("The 'try except' is finished")


#Try to open and write to a file that is not writable:
try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("something went wrong writing to the file")
    finally:
        f.close
except:
   print("something went wrong while opening the file")
       
#TypeError
 
"""if not type(x) is str:
   raise TypeError("only Strings are allowed")
"""
#custom exceptions
class JustNotCoolError(Exception):
   pass


try:
   raise JustNotCoolError("This just isn't cool")
   #raise Exception("I'm a custom exception")
except:
   print("no errors")
finally:
   print("I'm going to print anyways")
