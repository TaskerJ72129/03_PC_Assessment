# import libraries if needed
import pandas

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
price_list = []
weight_kg_list = []

variable_dict = {
    "Item": item_list,
    "Weight(g)": weight_list,
    "Weight(kg)": weight_kg_list,
    "Price": price_list
}

# loop to get component, weight and price
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
    price = num_check("How much does it cost? $",
                      "The price must be a number more than 0",
                      float)
    weight_kg = weight / 1000

    # add item, weight and price to lists
    
    item_list.append(item_name)
    weight_list.append(weight)
    price_list.append(price)
    weight_kg_list.append(weight_kg)


variable_frame = pandas.DataFrame(variable_dict)
variable_frame = variable_frame.set_index('Item')

# Calculate cost of each component
variable_frame['Cost'] = variable_frame['Price']\
                         / variable_frame['Weight(kg)']

# Currency Formatting ( uses currency function)
add_dollars = ['Price', 'Cost']
for item in add_dollars:
    variable_frame[item] = variable_frame[item].apply(currency)

# ************************ Printing Area **************************

print(variable_frame)
