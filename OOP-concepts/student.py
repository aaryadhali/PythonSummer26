class Student:
    # class variable
    # shared among all instances of classes
    # they are defined outside of construcor
    # benefit: allows you to share data among all objects in a class
    
    class_year = 2024
    num_students = 0

    # can write whatever you want within constructor
    # this code will always be executed when you
    # instantiate the class
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # when modifying a class variable use the class name instead of self
        # since it gets executed everytime init is called 
        # count or num_students will execute

        Student.num_students +=1


student1 = Student("spongbob", 30)
student2 = Student("patrick", 35)
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)


print(student2.name)
print(student2.age)
print(f"my graduating class of {Student.class_year} has {Student.num_students} students")

print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)