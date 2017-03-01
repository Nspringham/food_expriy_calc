#! python3


import datetime

# Print the current date
today = datetime.date.today()
print(today.strftime('Today\'s date: %d, %b %Y\n'))

# Dictionary containing food keys and their corresponding values
food = {'fudge_cake': 3,
        'fruit_coulis': 10,
        'GF_brownie': 3,
        'Honeycomb': 4,
        'Lemon_poss': 4,
        'Profiterol': 2,
        'Tiramisu': 3,
        'Vanilla_Cake': 3}

fudge = food['fudge_cake']
coulis = food['fruit_coulis']
brownie = food['GF_brownie']
honey = food['Honeycomb']
posset = food['Lemon_poss']
prof = food['Profiterol']
tiramisu = food['Tiramisu']
cheesecake = food['Vanilla_Cake']



def expiry_calc(item_name):

    today = datetime.date.today()
    aditionalDay = datetime.timedelta(days=item_name)
    newDay = today + aditionalDay
    print(newDay.strftime('--Expiry: %a, %d/%m/%Y--'))

# Calling the expiry() function with the 'variable' keyword e.g. expiry_calc(brownie) will output correctly.
def user_select():
    keyword_set = {'brownie', 'cheesecake', 'coulis', 'fudge', 'honey', 'prof', 'posset', 'tiramisu'}
    print(keyword_set)
    while True:
        user_input = input('\nPlease enter food item:\n')
        if user_input == "help":
            print(keyword_set)
        elif user_input not in keyword_set:
            print('entry incorrect')
        elif user_input == "brownie":
            expiry_calc(brownie)
        elif user_input == "fudge":
            expiry_calc(fudge)
        elif user_input == "coulis":
            expiry_calc(coulis)
        elif user_input == "honey":
            expiry_calc(honey)
        elif user_input == "posset":
            expiry_calc(posset)
        elif user_input == "tiramisu":
            expiry_calc(tiramisu)
        elif user_input == "cheesecake":
            expiry_calc(cheesecake)
        elif user_input == "prof":
            expiry_calc(prof)
        else:
            print('error occured')

user_select()
