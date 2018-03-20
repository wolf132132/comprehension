text = input("Please enter your text: ")

output = []
for x in text.split():
    output.append(len(x))
print(output)

# output = []
info = [len(x) for x in text.split(" ")]
print (info)

output = []
for x in text.split():
    output.append((x, len(x)))
print(output)

#this will return a set. set will contain duplicated elements
info_length = {(x, len(x)) for x in text.split()}
print(info_length)

