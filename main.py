MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 230,
    "milk": 340,
    "coffee": 1100,
    "money": 0.00
}


prompto = False
select_coffee = {}

def process_coins(param, coffee_type):
    def round_half_up(n, decimals=0):
        multiplier = 10 ** decimals
        return int(n * multiplier + 0.5) / multiplier
    balance = 0.0
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    inserted_quarters = input(f" How many quarters:")
    inserted_dimes = input(f" How many dimes:")
    inserted_nickles = input(f" How many nickles:")
    inserted_pennies = input(f" How many pennies:")
    total = (float(inserted_quarters) * quarters) + (float(inserted_dimes) * dimes) + (float(inserted_nickles) * nickles) + (float(inserted_pennies) * pennies)

    if total < param['cost']:
        balance = round_half_up(param['cost'] - total, 2)
    if total > param['cost']:
        balance = round_half_up(total - param['cost'], 2)

    if total == param['cost']:
        print(f"Here is your {coffee_type}. Enjoy!")
        print(f"Resources report before purchasing {coffee_type}: {resources}")
        if coffee_type == 'espresso':
            resources['water'] = resources['water'] - param['ingredients']['water']
            resources['coffee'] = resources['coffee'] - param['ingredients']['coffee']
        else:
            resources['water'] = resources['water'] - param['ingredients']['water']
            resources['milk'] = resources['milk'] - param['ingredients']['milk']
            resources['coffee'] = resources['coffee'] - param['ingredients']['coffee']
        resources['money'] += total
        print(f"Resources report after purchasing {coffee_type}: {resources}")
    elif total > param['cost'] and resources['money'] > balance:
        print(f"Here is ${balance} dollars in change")
        print(f"Here is your {coffee_type}. Enjoy!")
        print(f"Resources report before purchasing {coffee_type}: {resources}")
        if coffee_type == 'espresso':
            resources['water'] = resources['water'] - param['ingredients']['water']
            resources['coffee'] = resources['coffee'] - param['ingredients']['coffee']
        else:
            resources['water'] = resources['water'] - param['ingredients']['water']
            resources['milk'] = resources['milk'] - param['ingredients']['milk']
            resources['coffee'] = resources['coffee'] - param['ingredients']['coffee']
        resources['money'] = (resources['money'] + total) - balance
        print(f"Resources report after purchasing {coffee_type}: {resources}")
    else:
        if resources['money'] < balance :
            print(f"Sorry that's not enough balance. Money refunded.")
        else:
            print(f"Sorry that's not enough money. Money refunded.")

def check_and_update_resources(param, coffee_type):
    water = True
    coffee = True
    milk = True
    if 'milk' not in param['ingredients']:
        water = resources["water"] >= param['ingredients']['water']
        coffee = resources["coffee"] >= param['ingredients']['coffee']
    else:
        water = resources["water"] >= param['ingredients']['water']
        coffee = resources["coffee"] >= param['ingredients']['coffee']
        milk = resources["milk"] >= param['ingredients']['milk']

    lists = [
        {'name': 'water', 'state': water},
        {'name': 'coffee', 'state': coffee},
        {'name': 'milk', 'state': milk},
    ]

    if water and coffee and milk:
        if 'milk' not in param['ingredients']:
            process_coins(param, coffee_type)
            return True
        else:
            process_coins(param, coffee_type)
            return True
    else:
        for item in lists:
            if item['state'] == False:
                try:
                    print(f"Sorry there is not enough {item['name']}.")
                except:
                    return
        return False




while prompto == False:
    coffee_type = input("What would you like? (espresso/latte/cappuccino):").lower()

    if coffee_type == 'off':
        break
    elif coffee_type == 'espresso':
        print(f"{coffee_type} details : {MENU[coffee_type]}")
        select_coffee = MENU[coffee_type]
        # resources["money"] += MENU[coffee_type]["cost"]
        if check_and_update_resources(MENU[coffee_type], coffee_type):
            prompto = True
        else:
            prompto = False

    elif coffee_type == 'latte':
        print(f"{coffee_type} details : {MENU[coffee_type]}")
        select_coffee = MENU[coffee_type]
        # resources["money"] += MENU[coffee_type]["cost"]
        if check_and_update_resources(MENU[coffee_type], coffee_type):
            prompto = True
        else:
            prompto = False

    elif coffee_type == 'cappuccino':
        print(f"{coffee_type} details : {MENU[coffee_type]}")
        select_coffee = MENU[coffee_type]
        # resources["money"] += MENU[coffee_type]["cost"]
        if check_and_update_resources(MENU[coffee_type], coffee_type):
            prompto = True
        else:
            prompto = False

    elif coffee_type == 'report':
        print(f"{resources}")
        # if check_and_update_resources(MENU[coffee_type], coffee_type):
        #     prompto = True
        # else:
        prompto = False

    else:
        print(f"No such Coffee, Please choose your coffee again:")







