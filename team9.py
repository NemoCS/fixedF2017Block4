team_name = 'The best'
strategy_name = 'T for T v2'
strategy_description = 'Counters all b and all c'
    
def move(my_history, their_history, my_score, their_score):
    if my_score < their_score:
        return 'b'
    if len(their_history) == 0:
        return 'b'
    elif their_history(-1) == 'b':
        return 'b'
    if len(their_history) == 5:
       if their_history(-5) == 'ccccc':
            return 'b'
    if len(their_history) == 6:
        if their_history(-6) == 'cccbbc':
            return 'b'
    else:
        return 'c'
            