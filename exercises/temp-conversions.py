# Fahrenheit = Celsius × (9 / 5) + 32
# Celsius = (Fahrenheit - 32) × (5 / 9)

def Fahrenheit_to_Celcius(fahrenheit):
    return round((fahrenheit - 32) * (5 / 9), 2)

def Celcius_to_Fahrenheit(celsius):
    return round(celsius * (9 / 5) + 32, 2)

print(Fahrenheit_to_Celcius(76))
print(Celcius_to_Fahrenheit(200))