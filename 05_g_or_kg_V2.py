
valid = False 
while not valid:

    # ask for profit goal...
    weight = input("weight(g or kg):")

    # check if first character is $...
    if weight[-1] == "g":
        kg_or_g = "g"
        # Get amount (everything before the kg)
        amount = weight[:-1]

        valid = True
    # check if the last character is %
    elif weight [-1] == "kg":
        kg_or_g = "kg"
        weight_kg = (float(weight))

        
        Valid = True

    else:
        print("Please enter _kg or _g")
        

weight = weight[:-1]
weight_g = (float(weight))


print(kg_or_g)
print(weight)
print(weight_g)
print(weight_kg)
