
valid = False 
while not valid:
    try:
        # ask for g or kg
        weight = input("weight(g or kg):")

        # check if the last 2 characters are kg
        if weight[-2:] == "kg":
            amount = weight[:-2]
            weight_kg = (float(amount))
            weight_g = weight_kg * 1000

            valid = True

        # if its not kg check if last character is g
        elif weight[-1] == "g":
            # Get amount (everything before the g)
            amount = weight[:-1]
            weight_g = (float(amount))
            weight_kg = weight_g / 1000

            valid = True


        else:
            print("Please enter _kg or _g")

    except ValueError:
        print("Please enter _kg or _g")
        
print("Weight_g")
print(weight_g)
print("Weight_kg")
print(weight_kg)
