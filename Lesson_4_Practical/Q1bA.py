def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

fahrenheit = float(input(f"Enter a temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"The temperature in Celsius is: {celsius:.2f} degrees")
