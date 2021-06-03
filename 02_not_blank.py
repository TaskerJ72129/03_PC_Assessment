# Checks that string response is not blank
def not_blank(question, error):

    valid = False 
    while not valid:
        response = input(question)

        if response == "":
            print("{}.  \nPlease try again.\n".format(error))
            continue

        return response


# Main routine goes here
get_item = not_blank("Item name: ", "The item name can't be blank")


# printing area
print("Item name: {}".format(get_item))
