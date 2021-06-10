# import libraries if needed


# ---- Functions go here ----

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

# Checks that response is not blank
def not_blank(question, error):

    valid = False 
    while not valid:
        response = input(question)

        if response == "":
            print("{}.  \nPlease try again.\n".format(error))
            continue

        return response


# ***** Main routine goes here *****

# instructions

# ask for budget

