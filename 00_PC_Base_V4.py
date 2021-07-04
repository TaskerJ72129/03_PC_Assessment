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

        # if the chosen option is not valid, set in_valid to no 
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
        print("**** Instructions ****")
        print("instructions go here")
        print()

    return ""

# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# Main routine goes here
# Set up dictionaries and lists

item_list = []
weight_list = []
cost_list = []
weight_kg_list = []

variable_dict = {
    "Item": item_list,
    "Weight(g)": weight_list,
    "Weight(kg)": weight_kg_list,
    "Cost": cost_list
}

# ask for budget
budget = num_check("What is your budget? $",
                   "The budget must be a number more than 0",
                   float)

# loop to get component, weight and Cost
item_name = ""
while item_name.lower() != "xxx":

    print()
    item_name = not_blank("Item name: ",
                          "The component name can't be "
                          "blank.")
    if item_name.lower() == "xxx":
        break

    weight = num_check("weight(g):",
                       "The weight must be a number "
                       "more than zero",
                       float)
    cost = num_check("How much does it cost? $",
                     "The Cost must be a number more than 0",
                     float)
    # convert g to kg
    weight_kg = weight / 1000

    # add item, weight and Cost to lists
    item_list.append(item_name)
    weight_list.append(weight)
    cost_list.append(cost)
    weight_kg_list.append(weight_kg)


variable_frame = pandas.DataFrame(variable_dict)
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

number = 1

a = 0
d = variable_frame.iat[a,0]
print(d)
s = d[1:]
print(s)
c = (float(s))
print(budget)

while c > budget:
    a += 1

# recommendation
recommendation = variable_frame.iloc[[a]]


# ************************ Printing Area **************************
print()
print("budget: ${}".format(budget))
print()
print(variable_frame)
print()
print("**** Recommendation ****")
print(recommendation)

