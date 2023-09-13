import pandas


def string_checker(question, valid_responses):
    error = "Please input a valid response "

    while True:
        response = input(question).lower()

        if response == 'xxx':
            return 'xxx'  # Return 'xxx' immediately to exit the loop

        if response in valid_responses:
            return response

        print(error)


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# calculate burger price
def calc_burger_price(var_burger):
    price = 0
    # price is $8.50 for Burger 1
    if var_burger == "meat lover":
        price = 8.50

    # price is $12.50 for Burger 2
    elif var_burger == "black meat":
        price = 12.50

    # price is $15.50 for Burger 3
    elif var_burger == "banana jizz filled":
        price = 15.50

    # price is $18.50 for Burger 4
    elif var_burger == "zinger":
        price = 18.50

    # price is $22.50 for Burger 5
    elif var_burger == "tender girls":
        price = 22.50

    # price is $24.50 for Burger 6
    elif var_burger == "tender boys":
        price = 24.50

    # price is $26.50 for Burger 7
    elif var_burger == "tender blender":
        price = 26.50

    # price is $28.50 for Burger 8
    elif var_burger == "bouncy meat":
        price = 28.50

    # price is $31.50 for Burger 9
    elif var_burger == "juicy breast":
        price = 31.50

    # price is $40.50for Burger 10
    elif var_burger == "hot mouth":
        price = 40.50

    return price


burger_sold = 0
total_burger_cost = 0
burger_sold_list = []
burger_price_list = []
yes_no_list = ["yes", "no"]
all_burger = ["meat lover", "black meat", "banana jizz filled", "zinger", "tender girls", "tender boys",
              "tender blender", "bouncy meat", "juicy breast", "hot mouth"]
all_burger_costs = [8.50, 12.50, 15.50, 18.50, 22.50, 24.50, 26.50, 28.50, 31.50, 40.50]


# program to display the burger menu
burger_program_dict = {
    "Burger": all_burger,
    "Burger Price": all_burger_costs,
    }

burger_program_frame = pandas.DataFrame(burger_program_dict)
burger_program_frame = burger_program_frame.set_index('Burger')
burger_program_frame['Burger Price'] = burger_program_frame['Burger Price'].apply(currency)


while True:
    # program starts here
    print("---- Burger Menu ----")
    print()

    # output table with burger data
    print(burger_program_frame)
    print()

    # search for burger price from cal_burger_price
    burger_choice = string_checker("Which Burger would you like to order(type 'xxx' to quit): ",
                                   all_burger)

    if burger_choice == "xxx":
        break  # Exit the loop when 'xxx' is entered
    # print what the user entered
    print("User entered:", burger_choice)

    # calculate the burger price from the list based burger choice
    burger_price = calc_burger_price(burger_choice)
    print("You chose {}, Burger Price ${:.2f}".format(burger_choice, burger_price))
