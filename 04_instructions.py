# String check
def string_check(choice, options):

    for var_list in options:

        # if the snack is in one of the lists, return the full name
        if choice in var_list:

            # Get full name of snack and put it
            # in title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen option is not valid, set in_valid to no 
        else:
            is_valid = "no"

    # if the snacks is not OK - ask question again.
    if is_valid == "yes":
        return chosen
    else:
        print("Please enter a valid option\n")
        return "invalid choice"


# function to show instructions if necessary
def instructions(options):

    show_help = "invalid choice"
    while show_help == "invalid choice":
        show_help = input("Would you like to read the instructions? ").lower()
        show_help = string_check(show_help, options)

    if show_help == "Yes":
        print()
        print("**** Mega Movie Fundraiser Instructions ****")
        print("instructions go here")
        print()

    return ""

yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

instructions(yes_no)