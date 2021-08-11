
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
    try:
        # ask for g or kg
        weight = input("weight(g or kg):")

        # check if the last 2 characters are kg
        if weight[-2:] == "kg":
            type = "kg"
            amount = weight[:-2]
            weight_kg = (float(amount))
            weight_g = weight_kg * 1000

            valid = True

        # if its not kg check if last character is g
        elif weight[-1] == "g":
            type = "g"
            # Get amount (everything before the g)
            amount = weight[:-1]
            weight_g = (float(amount))
            weight_kg = weight_g / 1000

            valid = True

        else:
            amount = weight
            weight = (float(amount))
            type = "unknown"

        if type == "unknown" and amount <= 5:
            type = yes_no("Do you mean {:.2f}kg"
                          "? , y / n ".format(amount, amount))
            
    


    except ValueError:
        print("Please enter _kg or _g")
        
print("Weight_g")
print(weight_g)
print("Weight_kg")
print(weight_kg)
