print("Cost of Each SandWich: $5")

print("List of toppings available: \nOnions \nLattice \nTomato \nPeppers \nTomatoes")

print("Select any there available toppings")

first_topping = input("Enter first topping: ")
second_topping = input("Enter second topping: ")
third_topping = input("Enter third topping: ")

sandwiches_required = int(input("How many Sanwiches you want?"))

totalCost = sandwiches_required * 5

print("Total bill: ", totalCost , "$",sep='')