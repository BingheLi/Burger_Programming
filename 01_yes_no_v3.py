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


**************************''')


def string_checker(question, valid_responses):
    error = "Please input a valid response "

    while True:
        response = input(question).lower()

        if response == 'xxx':
            return 'xxx'  # Return 'xxx' immediately to exit the loop

        if response in valid_responses:
            return response

        print(error)


yes_no_list = ["yes", "no"]
# main routine goes here
while True:
    want_instructions = string_checker("Do you want to read the instructions (yes/no): ",
                                       yes_no_list)
    if want_instructions == "yes":
        show_instructions()
    else:
        print("program continues...")
        pass
