team_name = "Team16"

strategy_name = "Lets see if this works"

strategy_description = "Luck"

import random

#my_history = ""

def move(my_history, their_history, my_score, their_score):

    if len(their_history)==0:
        return random.choice([ "c ", "b" ])

    elif len(their_history)==1:
        return random.choice([ "c ", "b" ])

    elif len(their_history)==2:
        return random.choice([ "c ", "b" ])

    elif len(their_history)==03:
        return random.choice([ "c ", "b" ])

    elif their_history[-3] == ( "b", "b", "b"):
        return "c"

    elif their_history[-3] == ("c", "c", "c"):
        return "b"

    elif their_history[-3] == ("b", "c", "b"):
        return "c"
    
    elif my_history[-4] == ("c", "c","c", "c"):
        return "b"
    else:
        return "b"

