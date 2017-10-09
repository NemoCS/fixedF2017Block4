team_name = 'Vindictish'
strategy_name = 'I shall forgeev'
strategy_description = 'meanie gets meanie'

def move(my_history, their_history, my_score, their_score):
    if len(my_history) == 0:
        return 'c'
    elif 'b' not in their_history(-5):
        return 'c'
    elif 'b' in their_history: 
        return 'b'
    else:
        return 'c'
            