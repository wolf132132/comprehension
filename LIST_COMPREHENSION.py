numbers = [1, 2, 3, 4, 5, 6]

# # squares = [number ** 2 for number in numbers]
# squares = [number ** 2 for number in numbers]
# print (squares)

text = "what have the romans ever done for us"

# capitals = [char.upper() for char in text.split]
capitals = [char.upper() for char in text.split(" ")]
print (capitals)

lower_case_text = [word for word in text.split()]
print (lower_case_text)
