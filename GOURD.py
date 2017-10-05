team_name = 'GOURD'
strategy_name = 'GourdStrategy'
strategy_description = 'Collude until enemy betrays, then betray every time with a chance to forgive.'
import random
class betrayed:
    pass
    #betrayed.betrayed- if betrayed, betray every time, but small chance to forgive


def move(my_history, their_history, my_score, their_score):
    
    if len(their_history) == 0:
        return 'c'
    elif their_history[-1] == 'b':
        return 'b'
        betrayed.betrayed = True
    elif their_history [-1] == 'c' and betrayed.betrayed == True:
        if random.random > .5:
            return "c"
            betrayed.betrayed == False
        else:
            return "b"
    else:
        return 'c'