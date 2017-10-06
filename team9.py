team_name = 'Vindictish'
strategy_name = 'I shall forgeev'
strategy_description = 'meanie gets meanie'
import random
def move(my_history, their_history, my_score, their_score):
    if len(my_history) == 0:
        return 'c'
    elif 'b' in their_history(-3):
        if random.random() > 0.1:
            return 'b'
        else:
            return 'c'
    else:
        return 'c'
            