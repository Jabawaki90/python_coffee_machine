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
    "money": 0
}

prompto = False
select_coffee = {}

def check_and_update_resources(param):
    water = True
    coffee = True
    milk = True
    if 'milk' not in param['ingredients']:
        water = resources["water"] >= param['ingredients']['water']
        coffee = resources["coffee"] >= param['ingredients']['coffee']
        # milk = resources["milk"] >= param['ingredients']['milk']
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
            resources['water'] = resources["water"] - param['ingredients']['water']
            resources['coffee'] = resources["coffee"] - param['ingredients']['coffee']
            # resources['milk'] = resources["milk"] - param['ingredients']['milk']
            resources['money'] += param['cost']
            print('all true')
            return True
        else:
            resources['water'] = resources["water"] - param['ingredients']['water']
            resources['coffee'] = resources["coffee"] - param['ingredients']['coffee']
            resources['milk'] = resources["milk"] - param['ingredients']['milk']
            resources['money'] += param['cost']
            print('all true')
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
        if check_and_update_resources(MENU[coffee_type]):
            prompto = True
        else:
            prompto = False

    elif coffee_type == 'latte':
        print(f"{coffee_type} details : {MENU[coffee_type]}")
        select_coffee = MENU[coffee_type]
        # resources["money"] += MENU[coffee_type]["cost"]
        if check_and_update_resources(MENU[coffee_type]):
            prompto = True
        else:
            prompto = False

    elif coffee_type == 'cappuccino':
        print(f"{coffee_type} details : {MENU[coffee_type]}")
        select_coffee = MENU[coffee_type]
        # resources["money"] += MENU[coffee_type]["cost"]
        if check_and_update_resources(MENU[coffee_type]):
            prompto = True
        else:
            prompto = False

    elif coffee_type == 'report':
        print(f"{resources}")
        if check_and_update_resources(MENU[coffee_type]):
            prompto = True
        else:
            prompto = False

    else:
        print(f"No such Coffee, Please choose your coffee again:")







