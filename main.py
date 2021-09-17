name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
ticket_price = 0

if age <= 4:
    ticket_price = 0
elif age <= 18:
    ticket_price = 1.50
elif age >= 60:
    ticket_price = 1
else:
    ticket_price = 2

print(f"The Customer: {name} has: {age} years and his ticket cost is: $ {ticket_price}")
