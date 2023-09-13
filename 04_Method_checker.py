# functions go here
def eat_option(question):

    while True:
        response = input(question).lower()

        if response == "dine in" or response == "di":
            return "dine in"

        elif response == "delivery" or response == "de":
            return "delivery"

        else:
            print("Please choose a valid eat method")


# main routine goes here
while True:
    eat_method = eat_option("Choose a method (Dine in "
                            "or Delivery): ")

    print("You chose", eat_method)
    print()
