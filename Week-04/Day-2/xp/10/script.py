while True:
    topping = input("what toppings would you like on your pizza ? (write quit when you finish) : ")

    if topping == "quit":
        break

top_list = list(topping.split(" "))

print(top_list)

# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).