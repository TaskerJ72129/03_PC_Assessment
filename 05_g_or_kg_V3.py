
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
        
        
        try:
            # Check amount is a number more that zero
            if weight_g <= 0:
                print("Please enter a number above 0")
                valid = False

            if weight_kg <= 0:
                print("Please enter a number above 0")
                valid = False

            else:
                valid = True

        except ValueError:
            print("Please enter _kg or _g")
            valid = False


        else:
            print("Please enter _kg or _g")

    except ValueError:
        print("Please enter _kg or _g")
        
print("Weight_g")
print(weight_g)
print("Weight_kg")
print(weight_kg)
