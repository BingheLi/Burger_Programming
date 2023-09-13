import pandas


# functions go here
# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


def burger_combo(question):
    while True:
        response = input(question).lower()

        if response == "1":
            return "Meat Lover"

        if response == "2":
            return "Black Meat"

        if response == "3":
            return "Banana Jizz Filled"

        if response == "4":
            return "Zinger"

        if response == "5":
            return "Tender Girls"

        if response == "6":
            return "Tender Boys"

        if response == "7":
            return "Tender Blender"

        if response == "8":
            return "Bouncy Meat"

        if response == "9":
            return "Juicy Breast"

        if response == "10":
            return "Hot Mouth"

        if response == "xxx":
            return "Quit"

        else:
            print("Please choose a valid burger")


def calc_burger_price(var_burger):
    # price is $8.50 for Burger 1
    if var_burger == "Meat Lover":
        price = 8.50

    # price is $12.50 for Burger 2
    elif var_burger == "Black Meat":
        price = 12.50

    # price is $15.50 for Burger 3
    elif var_burger == "Banana Jizz Filled":
        price = 15.50

    # price is $18.50 for Burger 4
    elif var_burger == "Zinger":
        price = 18.50

    # price is $22.50 for Burger 5
    elif var_burger == "Tender Girls":
        price = 22.50

    # price is $24.50 for Burger 6
    elif var_burger == "Tender Boys":
        price = 24.50

    # price is $26.50 for Burger 7
    elif var_burger == "Tender Blender":
        price = 26.50

    # price is $28.50 for Burger 8
    elif var_burger == "Bouncy Meat":
        price = 28.50

    # price is $31.50 for Burger 9
    elif var_burger == "Juicy Breast":
        price = 31.50

    # price is $40.50for Burger 10
    elif var_burger == "Hot Mouth":
        price = 40.50

    else:
        price = 0

    return price


# main routine starts here
# set maximum number of tickets below

MAX_BURGERS = 5

# dictionaries to hold ticket details
all_burger = ["1. Meat Lover", "2. Black Meat", "3. Banana Jizz Filled", "4. Zinger", "5. Tender Girls", "6. Tender Boys", "7. Tender Blender", "8. Bouncy Meat", "9. Juicy Breast", "10. Hot Mouth"]
all_burger_costs = [8.50, 12.50, 15.50, 18.50, 22.50, 24.50, 26.50, 28.50, 31.50, 40.50]


burger_program_dict = {
    "Burger:": all_burger,
    "Price": all_burger_costs,
}

burger_program_frame = pandas.DataFrame(burger_program_dict)
burger_program_frame = burger_program_frame.set_index('Burger:')

burger_program_frame['Price'] = burger_program_frame['Price'].apply(currency)

# loop to sell tickets
burgers_sold = 0
total_cost = 0
while burgers_sold < MAX_BURGERS:
    print("---- Burger Menu ----")
    print()

    # output table with ticket data
    print(burger_program_frame)
    print()
    burger = burger_combo("Please enter the burger you want or 'xxx' to quit: ")
    burger_cost = calc_burger_price(burger)
    total_cost += burger_cost
    if burger == 'Quit':
        break
        print("You chose {}" .format(burger))
    else:
        print("You chose {}, Burger Price ${:.2f}".format(burger, burger_cost))
    burgers_sold += 1


# Output number of pizzas sold
if burgers_sold == MAX_BURGERS:
    print("Congratulations you have sold all the burger")
    print("The total price would be ${:.2f} ".format(total_cost))
else:
    print("You have sold {} burger/s. There is {} burger/s "
          "remaining".format(burgers_sold, MAX_BURGERS - burgers_sold))
    print("The total price would be ${:.2f} ".format(total_cost))