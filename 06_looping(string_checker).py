import pandas


# functions go here
# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# main routine starts here
# set maximum number of tickets below
MAX_BURGERS = 5

# dictionaries to hold ticket details
all_burger = ["Meat Lover", "Black Meat", "Banana Jizz Filled", "Zinger", "Tender Girls","Tender Boys", "Tender Blender", "Bouncy Meat", "Juicy Breast", "Hot Mouth"]
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
while burgers_sold < MAX_BURGERS:
    print("---- Burger Menu ----")
    print()

    # output table with ticket data
    print(burger_program_frame)
    print()
    burger = input("Please enter the burger you want or 'xxx' to quit: ")
    print()
    if burger == 'xxx':
        break

    burgers_sold += 1


# Output number of pizzas sold
if burgers_sold == MAX_BURGERS:
    print("Congratulations you have sold all the burger")
else:
    print("You have sold {} burger/s. There is {} burger/s "
          "remaining".format(burgers_sold, MAX_BURGERS - burgers_sold))