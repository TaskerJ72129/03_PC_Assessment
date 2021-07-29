
valid = False 
while not valid:

    # ask for profit goal...
    weight = input("weight(g):")

    # check if first character is $...
    if weight[-1] == "g":
        kg_or_g = "g"
        # Get amount (everything before the g)
        amount = weight[1:]
        valid = True
    # check if the last character is %
    elif weight [-1] == "kg":
        kg_or_g = "kg"
        # Get amount (everything before the kg)
        amount = weight[:-1]
        Valid = True

    else:
        print("Please enter _kg or _g")
        

weight = weight[:-1]

print(kg_or_g)
print(weight)

