# checks that users enter a valid response (eg yes / no
# cash / credit) based on a list of options
def string_checker(question, valid_responses):
    error = "Please input a valid response "

    while True:
        response = input(question).lower()

        if response == 'xxx':
            return 'xxx'  # Return 'xxx' immediately to exit the loop

        if response in valid_responses:
            return response

        print(error)


# main routine starts here
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]
method_list = ["dine in", "delivery"]

want_instructions = string_checker("Do you want to read the instructions (y/n): ",
                                   yes_no_list)
print("You chose", want_instructions)


pay_method = string_checker("Choose a payment method (cash / credit): ",
                            payment_list)
print("You chose", pay_method)

eat_method = string_checker("Choose a method (dine in / "
                            "delivery): ",
                            method_list)
print("You chose", eat_method)
