print("Welcome to the sandwich shop!")
lst = ['Onions', 'Lettuce', 'Tomato', 'Olives', 'Peppers', 'Tomatoes']
toppings = [x for x in input("Please choose 3 fillings from:", lst).split()]
print("Selected toppings are: ", toppings)
quantity = int(input("How many sandwiches would you like?"))

total = quantity * 5

print("Your total is: $", total)

