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


# function to show instructions if necessary
def instructions(options):

    show_help = "invalid choice"
    while show_help == "invalid choice":
        show_help = input("Do you want to read the instructions? ").lower()
        print()
        show_help = string_check(show_help, options)

    if show_help == "Yes":
        print("****  Price Comparison Instructions ****")
        print("Price comparison can be used to compare items prices and" 
              "recommend the best choice"
              ""
              "first enter budget"
              "then enter item name, weight and cost of all the items you want"
              "type when you are done"
             )  
        print()

    return ""

yes_no = [
    ["yes", "y"],
    ["no", "n"]
]
# Loop to make testing faster...
for item in range(0,6):
    instructions(yes_no)