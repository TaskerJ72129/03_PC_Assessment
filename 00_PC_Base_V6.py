# import libraries if needed
import pandas

# ---- Functions go here ----


# String check
def string_check(choice, options):

    for var_list in options:

        # if it is in one of the lists, return the full name
        if choice in var_list:

            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen option is not valid, set is_valid to no 
        else:
            is_valid = "no"

    # if it is not OK - ask question again.
    if is_valid == "yes":
        return chosen
    else:
        print("Please enter a valid option\n")
        return "invalid choice"


# Checks that string response is not blank
def not_blank(question, error):

    valid = False 
    while not valid:
        response = input(question)

        if response == "":
            print("{}.  \nPlease try again.\n".format(error))
            continue

        return response


# checks that input is either a float or an integer that is more than 0.
# Takes in custom error messages
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# function to show instructions if necessary
def instructions(options):

    show_help = "invalid choice"
    while show_help == "invalid choice":
        show_help = input("Do you want to read the instructions? ").lower()
        print()
        show_help = string_check(show_help, options)

    if show_help == "Yes":
        print("****  Price Comparison Instructions ****")
        print("Price comparison can be used to compare items prices and " 
              "recommend the best choice\n\n"
              "First enter your budget\n"
              "Then enter item name, weight and cost of all the items you want\n"
              "Type xxx where it asks for item when you are done\n"
              "it will print out a list with all the items "
              "and then the recommended choice will be below that"
             )  
        print()

    return ""

# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# Main routine goes here
# Set up dictionaries and lists


yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

item_list = []
weight_g_list = []
cost_list = []
weight_kg_list = []

variable_dict = {
    "Item": item_list,
    "Weight(g)": weight_g_list,
    "Weight(kg)": weight_kg_list,
    "Cost": cost_list
}

# instructions
instructions(yes_no)

# ask for budget
budget = num_check("What is your budget? $",
                   "The budget must be a number more than 0",
                   float)

# loop to get component, weight(g and kg) and Cost
item_name = ""
while item_name.lower() != "xxx":

    print()
    # Get item name and if there is an error print "The component name can't be blank" and ask again
    item_name = not_blank("Item name: ",
                          "The component name can't be "
                          "blank.")
    # if xxx break loop
    if item_name.lower() == "xxx":
        break

    valid = False 
    while not valid:

        # ask for g or kg
        weight = input("weight(g or kg):")

        # check if the last 2 characters are kg
        if weight[-2:] == "kg":
            last_chars = weight
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

    # Get cost and if there is an error print "the cost must be a number more than 0" and ask again
    cost = num_check("How much does it cost? $",
                     "The Cost must be a number more than 0",
                     float)

    # convert g to kg
    weight_kg = weight_g / 1000

    # add item, weight and Cost to lists
    item_list.append(item_name)
    weight_g_list.append(weight_g)
    cost_list.append(cost)
    weight_kg_list.append(weight_kg)

# create dataframe
variable_frame = pandas.DataFrame(variable_dict)
# set index as item
variable_frame = variable_frame.set_index('Item')

# Calculate cost of each component
variable_frame['Unit Price (per kg)'] = variable_frame['Cost']\
                         / variable_frame['Weight(kg)']

# sort unit price ascending
variable_frame = variable_frame.sort_values(by='Unit Price (per kg)')

# Currency Formatting ( uses currency function)
add_dollars = ['Cost', 'Unit Price (per kg)']
for item in add_dollars:
    variable_frame[item] = variable_frame[item].apply(currency)

point = 0
length = len(cost_list)
# find the lowest price per kg that is under budget
valid = "false"
while valid != "true":
    # find if all of the items cost more that the users budget 
    if point + 1 > length:
        point = "none"
        valid = "true"
        break

    # gets a certain point in the dataframe
    a = variable_frame.iat[point, 0]
    # takes off the $ in the front of the string
    b = a[1:]
    # converts the string to a float
    c = (float(b))
    # if the point in the dataframe is greater than the budget
    # then add 1 to point so it will try the next point in the dataframe
    if c > budget:
        point += 1
    else:
        valid = "true"

# recommendation
if point == "none":
    recommendation = "none of the items are within your budget"
    # recommendation is the highes point that is below budget
else:
    recommendation = variable_frame.iloc[[point]]


# ************************ Printing Area **************************
print()
print("budget: ${}".format(budget))
print()
print(variable_frame)
print()
print("**** Recommendation ****")
print(recommendation)

