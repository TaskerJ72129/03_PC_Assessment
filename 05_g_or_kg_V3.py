
# Checks that the user has entered yes / no to a question
def yes_no(question):

    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("Please enter either yes or no...\n")


valid = False 
while not valid:

        # ask for g or kg
        weight = input("weight(g or kg):")

        # check if the last 2 characters are kg
        if weight[-2:] == "kg":
            type = "kg"
            amount = weight[:-2]

        # if its not kg check if last character is g
        elif weight[-1] == "g":
            type = "g"
            amount = weight[:-1]

        else:
            amount = weight
            type = "unknown"

        try:
            # Check amount is a number more that zero
            amount = float(amount)
            if amount <= 0:
                print("Please enter _kg or _g")
                continue
        except ValueError:
            print("Please enter _kg or _g")
            continue


        if type == "unknown" and amount <= 5:

            yesorno = yes_no("Do you mean {}kg"
                          "? , (y / n): ".format(amount, amount))

            if yesorno == "yes":            
                type = "kg"
            else:
                type = "g"

        elif type == "unknown" and amount > 5:
            yesorno_g = yes_no("Do you mean {}g"
                    "? , (y / n): ".format(amount, amount))
            
            if yesorno_g == "yes":
                type = "g"
            else:
                type = "kg"

        if type == "kg":
            weight_kg = (float(amount))
            weight_g = weight_kg * 1000

            valid = True

        else:
            # Get amount (everything before the g)
            weight_g = (float(amount))
            weight_kg = weight_g / 1000

            valid = True



        
print("Weight_g")
print(weight_g)
print("Weight_kg")
print(weight_kg)
