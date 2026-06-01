class MyClass:
    x = 5

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

print(MyClass)

p1 = MyClass()
print(p1.x)

del p1

p2 = MyClass()
p3 = MyClass()
print(p2.x)
print(p3.x)


p1 = Person("Emil", 36)
print(p1.name)
print(p1.age)