# import libraries if needed
import pandas as pd

# ---- Functions go here ----

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

# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# Main routine goes here
# Set up dictionaries and lists

item_list = []
weight_list = []
Cost_list = []
weight_kg_list = []

variable_dict = {
    "Item": item_list,
    "Weight(g)": weight_list,
    "Weight(kg)": weight_kg_list,
    "Cost": Cost_list
}

# ask for budget
budget = num_check("What is your budget? $",
                   "The budget must be a number more than 0",
                   float)

# loop to get component, weight and Cost
item_name = ""
while item_name.lower() != "xxx":

    print()
    # get name, weight and item
    item_name = not_blank("Item name: ",
                          "The component name can't be "
                          "blank.")
    if item_name.lower() == "xxx":
        break

    weight = num_check("weight(g):",
                         "The weight must be a number "
                         "more than zero",
                         float)
    Cost = num_check("How much does it cost? $",
                      "The Cost must be a number more than 0",
                      float)
    weight_kg = weight / 1000

    # add item, weight and Cost to lists
    
    item_list.append(item_name)
    weight_list.append(weight)
    Cost_list.append(Cost)
    weight_kg_list.append(weight_kg)


variable_frame = pd.DataFrame(variable_dict)
variable_frame = variable_frame.set_index('Item')


# Calculate cost of each component
variable_frame['Unit Price (per kg)'] = variable_frame['Cost']\
                         / variable_frame['Weight(kg)']

# Currency Formatting ( uses currency function)
add_dollars = ['Cost', 'Unit Price (per kg)']
for item in add_dollars:
    variable_frame[item] = variable_frame[item].apply(currency)

# sort unit price ascending
variable_frame = variable_frame.sort_values(by='Unit Price (per kg)')

# ************************ Printing Area **************************
print()
print("budget: ${}".format(budget))
print()
print(variable_frame)
