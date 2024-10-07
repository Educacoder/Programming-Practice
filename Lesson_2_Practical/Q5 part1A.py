# Enter the age
age = int(input("Enter age: "))
# Check if the age is less than 16
if age < 16:
# if true, ticket price is 7.50
    ticket_price = 7.50
# else if age is greater or equal 16 and less than 65
elif age >= 16 and age < 65:
# if true, ticket price is 10.00
    ticket_price = 10.00
else:
# else ticket price is 5.50
    ticket_price = 5.50
# Print the ticket price for the age
print(f"The ticket price for age {age} is ${ticket_price:.2f}")