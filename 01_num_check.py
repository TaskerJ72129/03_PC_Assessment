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


# Main routine goes here
get_weight = num_check("How much does it weigh? (grams):",
                    "Please enter a number more than 0\n",
                    float)

# printing area
print("It weighs: {}g".format(get_weight))
