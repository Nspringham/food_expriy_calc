#! python3
# A small program to work out the expiry date of a product and print it to console.

import datetime

# Print the current date
today = datetime.date.today()
print(today.strftime('Today\'s date: %d, %b %Y\n'))


# food variables and their corresponding values
foods = dict(
    fudge = 3,
    coulis = 10,
    brownie = 3,
    honey = 4,
    posset = 4,
    prof = 2,
    tiramisu = 3,
    cheesecake = 3
    )

# Using food dictionary values with time delta method to aquire expiry date.
def expiry_calc(item_name):

    today = datetime.date.today()
    aditionalDay = datetime.timedelta(days=item_name)
    newDay = today + aditionalDay
    print(newDay.strftime('--Expiry: %a, %d/%m/%Y--'))



# Calling the expiry() function with the 'variable' keyword e.g. expiry_calc(brownie) will output correctly.
def user_select():
    keyword_set = {'brownie', 'cheesecake', 'coulis', 'fudge', 'honey', 'prof', 'posset', 'tiramisu'}
    print(", ".join(foods))
    while True:
        user_input = input('\nPlease enter food item:\n')
        if user_input == "help":
            print(", ".join(foods))
        elif user_input not in keyword_set:
            print('\nEntry incorrect')
        else:
            expiry_calc(foods[user_input])

if __name__ == '__main__':
    user_select()
