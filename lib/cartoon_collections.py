def roll_call_dwarves(list_dwarf):
    counter = 1
    for dwarf in list_dwarf:
        print(f"{counter}. {dwarf}")
        counter += 1

def summon_captain_planet(planeteer_calls):
    return [planteer.capitalize()+"!" for planteer in planeteer_calls]

def long_planeteer_calls(list_of_calls):
    max_length = 0
    for calls in list_of_calls:
        if len(calls) > max_length:
            max_length = len(calls)
    if max_length > 4:
        return True
    else:
        return False
    
def find_the_cheese(list_of_string):
    cheese_types = ["cheddar", "gouda", "camembert"]
    for string in list_of_string:
        if string in cheese_types:
            return string
    return None