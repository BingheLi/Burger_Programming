import pandas


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


burger_sold_list = []
sauce_sold_list = []
burger_choice = input("Burger: ")
burger_price = input("Burger Price: ")
sauce_choice = input("Sauce: ")
sauce_price = input("Sauce Price: ")
surcharge = input("Surcharge: ")
delivery_fee = input("Delivery Fee: ")
total_cost = 9.00
burger_price_list = []
sauce_price_list = []
# program to order burger and sent them in to a dataframe
burger_order_program_dict = {
    "Burger Sold": burger_sold_list,
    "Burger Price List": burger_price_list,
    }

burger_order_program_frame = pandas.DataFrame(columns=["Burger Sold", "Burger Price List"])
burger_order_program_frame = burger_order_program_frame.set_index('Burger Sold')
burger_order_program_frame['Burger Price List'] = burger_order_program_frame['Burger Price List'].apply(currency)


# program to order burger and sent them in to a dataframe
sauce_order_program_dict = {
    "Sauce Sold": sauce_sold_list,
    "Sauce Price List": sauce_price_list
}

sauce_order_program_frame = pandas.DataFrame(columns=["Sauce Sold", "Sauce Price List"])
sauce_order_program_frame = sauce_order_program_frame.set_index('Sauce Sold')
sauce_order_program_frame['Sauce Price List'] = sauce_order_program_frame['Sauce Price List'].apply(currency)


burger_sold_list.append(burger_choice)
burger_price_list.append(burger_price)
sauce_sold_list.append(sauce_choice)
sauce_price_list.append(sauce_price)

if not burger_order_program_frame.empty:
    burger_order_program_frame = pandas.concat([burger_order_program_frame, pandas.DataFrame(
        {"Burger Sold": [burger_choice], "Burger Price List": [burger_price]})], ignore_index=True)
else:
    burger_order_program_frame = pandas.DataFrame(
        {"Burger Sold": [burger_choice], "Burger Price List": [burger_price]})

if not sauce_order_program_frame.empty:
    sauce_order_program_frame = pandas.concat([sauce_order_program_frame, pandas.DataFrame(
        {"Sauce Sold": [sauce_choice], "Sauce Price List": [sauce_price]})], ignore_index=True)
else:
    sauce_order_program_frame = pandas.DataFrame({"Sauce Sold": [sauce_choice], "Sauce Price List": [sauce_price]})


# receipt
name = input("Name: ")
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
