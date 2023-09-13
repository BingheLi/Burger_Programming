import pandas
import random
from datetime import date
# functions go here


# shows instructions
def show_instructions():
    print('''\n
***** Instructions ******    
Welcome 
For each order, enter ...
- The person's name (can't be blank)
- Burger combo (name of the burger)
- Sauce (name of the sauce)
- Eat method (dine in / delivery)
- Payment method (cash / credit)

When you have entered all the users, press 'xxx' to quit.

The program will then display the order menu details 
including the cost of each burger and sauce, the fees+ 
and the total cost.

This information will also be automatically written to
a text file.

**************************''')


# checks that user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        # if the response is blank, outputs error
        if response == "":
            print("Sorry this can't be blank.  Please try again")
        else:
            return response


# checks users enter an integer to a given question
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer.")


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


# calculate sauce price
def calc_sauce_price(var_sauce):
    price = 0
    # price is $8.50 for Sauce 1
    if var_sauce == "suspicious mayo":
        price = 5.50

    # price is $12.50 for Sauce 2
    elif var_sauce == "smelly catchup":
        price = 4.50

    # price is $15.50 for Sauce 3
    elif var_sauce == "pickle juice":
        price = 3.50

    # price is $18.50 for Sauce 4
    elif var_sauce == "watery mustard":
        price = 3.50

    # price is $22.50 for Sauce 5
    elif var_sauce == "condensed vinegar":
        price = 2.50
    # price is $8.50 for Sauce 6
    if var_sauce == "lemon cream":
        price = 5.50

    # price is $12.50 for Sauce 7
    elif var_sauce == "rotten apple":
        price = 4.50

    # price is $15.50 for Sauce 8
    elif var_sauce == "dry onion":
        price = 3.50

    # price is $18.50 for Sauce 9
    elif var_sauce == "moist garlic":
        price = 3.50

    # price is $22.50 for Sauce 10
    elif var_sauce == "juicy bean":
        price = 2.50
    else:
        price = 0

    return price


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


# main routine starts
burger_sold = 0
sauce_sold = 0
total_burger_cost = 0
total_sauce_cost = 0
surcharge = 0
delivery_fee = 0
total_cost = 0

# string checker properties
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]
method_list = ["dine in", "delivery"]

# dictionaries to hold detail of order
burger_sold_list = []
sauce_sold_list = []
burger_price_list = []
sauce_price_list = []
burger_choice = []
sauce_choice = []

# dictionaries to hold burger and sauce details
all_burger = ["meat lover", "black meat", "banana jizz filled", "zinger", "tender girls", "tender boys",
              "tender blender", "bouncy meat", "juicy breast", "hot mouth"]
all_burger_costs = [8.50, 12.50, 15.50, 18.50, 22.50, 24.50, 26.50, 28.50, 31.50, 40.50]
all_sauce = ["suspicious mayo", "smelly catchup", "pickle juice", "watery mustard", "condensed vinegar",
             "lemon cream", "rotten apple", "dry onion", "moist garlic", "juicy bean"]
all_sauce_costs = [5.50, 4.50, 3.50, 3.50, 2.50, 5.50, 4.50, 3.50, 3.50, 2.50]

# program to display the burger menu
burger_program_dict = {
    "Burger": all_burger,
    "Burger Price": all_burger_costs,
    }

burger_program_frame = pandas.DataFrame(burger_program_dict)
burger_program_frame = burger_program_frame.set_index('Burger')
burger_program_frame['Burger Price'] = burger_program_frame['Burger Price'].apply(currency)

# program to order burger and sent them in to a dataframe
burger_order_program_dict = {
    "Burger Sold": burger_sold_list,
    "Burger Price List": burger_price_list,
    }

burger_order_program_frame = pandas.DataFrame(columns=["Burger Sold", "Burger Price List"])
burger_order_program_frame = burger_order_program_frame.set_index('Burger Sold')
burger_order_program_frame['Burger Price List'] = burger_order_program_frame['Burger Price List'].apply(currency)


# program to display the sauce menu
sauce_program_dict = {
    "Sauce": all_sauce,
    "Sauce Price": all_sauce_costs,
}

sauce_program_frame = pandas.DataFrame(sauce_program_dict)
sauce_program_frame = sauce_program_frame.set_index('Sauce')
sauce_program_frame['Sauce Price'] = sauce_program_frame['Sauce Price'].apply(currency)

# program to order burger and sent them in to a dataframe
sauce_order_program_dict = {
    "Sauce Sold": sauce_sold_list,
    "Sauce Price List": sauce_price_list
}

sauce_order_program_frame = pandas.DataFrame(columns=["Sauce Sold", "Sauce Price List"])
sauce_order_program_frame = sauce_order_program_frame.set_index('Sauce Sold')
sauce_order_program_frame['Sauce Price List'] = sauce_order_program_frame['Sauce Price List'].apply(currency)


# ask users if they want to see the instructions
want_instructions = string_checker("Do you want to read the instructions (yes/no): ",
                                   yes_no_list)
if want_instructions == "yes":
    show_instructions()
if want_instructions == "no":
    pass
# ask the user their name to start ordering
name = not_blank("Start ordering by entering your name: ")

confirm = "yes"

# display menu and calculate burger price
while confirm == "yes":
    print("---- Burger Menu ----")
    print()

    # output table with burger data
    print(burger_program_frame)
    print()

    burger_choice = []
    while burger_choice == []:


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
    # sent the data to the list that will be used to disply in the order summary
        burger_sold_list.append(burger_choice)
        burger_price_list.append(burger_price)
    # create dataframe( frame property can't use append so I search up on online and decided to use concat)
        if not burger_order_program_frame.empty:
            burger_order_program_frame = pandas.concat([burger_order_program_frame, pandas.DataFrame(
                {"Burger Sold": [burger_choice], "Burger Price List": [burger_price]})], ignore_index=True)
        else:
            burger_order_program_frame = pandas.DataFrame(
                {"Burger Sold": [burger_choice], "Burger Price List": [burger_price]})

    # ask if user want sauce
        extra = string_checker("Would you like some special sauce (yes/no): ",
                               yes_no_list)

    # if user answers "yes", pass to the next program and start sauce ordering
        if extra == "yes":
            pass

    # if users answers "no" set sauce sold to 1 which is the same as the max sauce.
    # so the loop sauce_sold < MAX_SAUCE won't run
        elif extra == "no":
            print("Thank you ordering, enjoy your juicy delicious burger")
            break

    # if user answer "yes" in the previous component this loop will run and user can start ordering
        print("---- Sauce List ----")
        print()

        # output table with sauce data
        print(sauce_program_frame)
        print()
        sauce_choice = string_checker("Which Sauce would you like to order(type 'xxx' to quit): ",
                                      all_sauce)

    # print out what users entered
        print("User entered:", sauce_choice)

    # calculate the sauce price from the list based burger choice
        sauce_price = calc_sauce_price(sauce_choice)
        print("You chose {}, Sauce Price ${:.2f}".format(sauce_choice, sauce_price))

    # sent the data to the list that will be used to disply in the order summary
        sauce_sold_list.append(sauce_choice)
        sauce_price_list.append(sauce_price)

    # create dataframe( frame property can't use append so I search up on online and decided to use concat)
        if not sauce_order_program_frame.empty:
            sauce_order_program_frame = pandas.concat([sauce_order_program_frame, pandas.DataFrame(
                {"Sauce Sold": [sauce_choice], "Sauce Price List": [sauce_price]})], ignore_index=True)
        else:
            sauce_order_program_frame = pandas.DataFrame({"Sauce Sold": [sauce_choice], "Sauce Price List": [sauce_price]})

        sauce_sold += 1

        print("------- Order -------")
        print(name)
        print("------- Burger -------")
        print(burger_order_program_frame)
        print("------- Sauce -------")
        print(sauce_order_program_frame)

    finalize = string_checker("Do you confirm your order(yes/no)", yes_no_list)
    if finalize == "yes":
        print("Order will be ready soon")

    else:
        print("Order canceled. Restarting...")
        burger_sold_list.clear()  # Clear burger data
        burger_price_list.clear()
        sauce_sold_list.clear()  # Clear sauce data
        sauce_price_list.clear()
        burger_order_program_frame = pandas.DataFrame(columns=["Burger Sold", "Burger Price List"])
        burger_order_program_frame = burger_order_program_frame.set_index('Burger Sold')
        sauce_order_program_frame = pandas.DataFrame(columns=["Sauce Sold", "Sauce Price List"])
        sauce_order_program_frame = sauce_order_program_frame.set_index('Sauce Sold')
        continue

    confirm = string_checker("Would you like to make another order?(yes/no)", yes_no_list)

# Calculate total burger cost
for burger_price in burger_price_list:
    total_burger_cost += burger_price

# Calculate total sauce cost
for sauce_price in sauce_price_list:
    total_sauce_cost += sauce_price

# ask user whether they want it delivered or dine in
eat_method = string_checker("Choose a method (dine in / "
                            "delivery($2 every kilometer up to 15 kilometers): ",
                            method_list)
print("You chose", eat_method)
if eat_method == "dine in":
    phone = num_check("Phone Number: ")
    print("See ya later")
else:
    phone = num_check("Phone Number: ")
    address = input("Address: ")
    delivery_distance = random.randint(2, 15)
    print("Delivery Distance is {} KM".format(delivery_distance))
    delivery_fee = delivery_distance*2
    print("The delivery fee will be ${:.2f}".format(delivery_fee))

# Calculate the total cost
total_burger_cost = sum(burger_price_list)
total_sauce_cost = sum(sauce_price_list)

# ask user if they want to pay with cash or credit
payment_method = string_checker("Choose a choose (cash / "
                                "credit(5%): ",
                                payment_list)
if payment_method == "cash":
    print("You choose Cash")
    total_cost = total_burger_cost + total_sauce_cost + delivery_fee
else:
    print("You choose Credit(there will be a 5% fee)")
    total_cost = (total_burger_cost + total_sauce_cost) * 1.05 + delivery_fee
    surcharge = (total_burger_cost + total_sauce_cost) * 1.05 - (total_burger_cost + total_sauce_cost)

# print out the order
# output table with  burger and sauce sold and their price
print("------- Order -------")
print(name)
print("------- Burger -------")
print(burger_order_program_frame)
print("------- Sauce -------")
print(sauce_order_program_frame)

# print out the fees
print("------- Fees -------")
print("Delivery Fee: {}".format(delivery_fee))
print("Surcharge: {}".format(surcharge))
print("----- Total Price -----")

# output total price
print("Total Price: ${:.2f}".format(total_cost))

