menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

for meal in menu:
    if "spam" not in meal:
        print(meal)
print(" ")

'''
#meal is an expression
#for meal in menu is an iteration
#if spam not in meal is a filter
'''
meals = [meal for meal in menu if "spam" not in meal and "chicken" not in meal]
print(meals)
print(" ")

'''
#The first if will be executed first. And then the second filter will exclude any meal
    contains both bacon and sausage
'''
fussy_meals = [meal for meal in menu if "spam" in meal or "egg" in meal
               if not ("bacon" in meal and "sausage" in meal)]
print(fussy_meals)
print(" ")

fussy_meals = [meal for meal in menu if "spam" in meal or "egg" in meal
               and not ("bacon" in meal and "sausage" in meal)]
print(fussy_meals)
print(" ")

# meals = [meal if "spam" not in meal else "a meal has been skipped" for meal in menu]
# print(meals)
# print(" ")
#
# x = 15
# expression = "Twelve" if x == 12 else "unknown"
# print(expression)
# print(" ")

'''
@create a set
@set does not have order
'''
elements = set()
for meal in menu:
    for item in meal:
        elements.add(item)
print(elements)