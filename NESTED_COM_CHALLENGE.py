burgers = ["beef", "chicken", "spicy beans"]
toppings = ["cheese", "egg", "beans", "spam"]

meals = [(burger, topping) for burger in burgers for topping in toppings]
print(meals)
print()


#first iterator runs first, returning the result beef and then the second iterator runs
#this is not a nested comprehension. Just a comprehension with two iterators
for meal in [(burger, topping) for burger in burgers for topping in toppings]:
    print(meal)
print()

#topping interator runs every item first
for meal in [[(burger, topping) for burger in burgers] for topping in toppings]:
    print(meal)