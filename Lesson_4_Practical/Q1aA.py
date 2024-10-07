def celsius_to_fahrenheit(celsius):
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

celsius = float(input(f"Enter a temperature in degrees Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"The temperature in Fahrenheit is: {fahrenheit:.2f} F")