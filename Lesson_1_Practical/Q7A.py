# Get the desired future value
future_value = float(input("Enter the desired future value ($): "))

# Get the annual interest rate
r = float(input("Enter the annual interest rate: "))

# Get the number of years that the money will appreciaten = int(input("Enter the number of years the money will grow: "))

# calculate the amount needed to deposit
present_value = future_value / (1.0 + r/100)**n

# Display the amount needed to deposit
print("You will need to deposit this amount:${:.2f} " .format(present_value))
#print(f"You will need to deposit this amount:${present_value:.2f} ")