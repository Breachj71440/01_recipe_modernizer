# ask user for amount
# ask user for unit
# check that unit is in dictionary

# if unit in dictionary, convert to ml

# if no unit given / unit is unknown, leave as is.


# ***** Function goes here *****
def unit_checker():

    unit_tocheck = input("Unit? ")

    # Abbreviation lists
    teaspoon = ["tsp", "teaspoon", "t"]
    tablespoon = ["tbs", "tablespoon", "T", "tbsp"]
    cup = ["C", "c"]
    ounce = ["O", "o", "oz"]
    pint = ["pt"]
    quart = ["q", "Q", "qt"]
    pound = ["lb"]
    litre = ["L"]


    if unit_tocheck == "":
        print("you chose {}".format(unit_tocheck))
        return unit_tocheck

    elif unit_tocheck == "T" or unit_tocheck.lower() in tablespoon:
        return "tbs"
    elif unit_tocheck.lower() in teaspoon:
        return "tsp"
    elif unit_tocheck == "C" or "c" in cup:
        return "cup"
    elif unit_tocheck == "O" or "o" or "oz" in ounce:
        return "ounce"
    elif unit_tocheck == "pt" in pint:
        return "pint"
    elif unit_tocheck == "q" or "Q" or "qt" in quart:
        return "quart"
    elif unit_tocheck == "lb" in pound:
        return "pound"
    elif unit_tocheck == "L" in litre:
        return "litre"

# ***** Main routine goes here *****
unit_central = {
    "tsp": 5,
    "tbs": 15,
    "cup": 237,
    "ounce": 28.35,
    "pint": 473,
    "quart": 946,
    "pound": 454,
    "litre": 1000
}

keep_going = ""
while keep_going == "":
    amount = eval(input("How much? "))
    amount = float(amount)

    # get unit and change it to match dictionary
    unit = unit_checker()

    if unit in unit_central:
        mult_by = unit_central.get(unit)
        amount = amount * mult_by
        print("amount in ml {}".format(amount))
    else:
        print("{} is unchanged".format(amount))

    keep_going = input("<enter> or q ")