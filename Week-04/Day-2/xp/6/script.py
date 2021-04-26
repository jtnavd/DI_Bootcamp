basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana") 
print("result 1 ", basket)

basket.remove("Blueberries") 
print("result 2 ", basket)

basket.insert(-1,"Kiwi")
print("result 3 ",basket)

basket.insert(0,"Apples")
print("result 4 ",basket)

count_i = basket.count("Apples")
print(count_i, "Apples")

for i in range(len(basket)):
    final_list = "\n".join(basket)
print(final_list)
print(basket)

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)
