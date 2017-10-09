####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Hoffman' # Only 10 chars displayed.
strategy_name = 'Curved Response'
strategy_description = "Choice dependent on opponent's multiple previous responses."
    
def move(my_history, their_history, my_score, their_score):
    if len(their_history) == 0:
        return 'c'
    elif len(their_history) == 1:
        return 'c'
    elif len(their_history) == 2:
        return 'c'
    elif len(their_history) >= 3:
        if their_history[-3:] == 'ccc':
                return 'c'
        elif their_history[-3:] == 'bbb':
                return 'b'
        elif their_history[-3:] == 'ccb':
                return 'c'
        elif their_history[-3:] == 'bbc':
                return 'b'
        elif their_history[-3:] == 'cbb':
                return 'b'
        elif their_history[-3:] == 'bcc':
                return 'c'
        elif their_history[-3:] == 'bcb':
                return 'b'
        elif their_history[-3:] == 'cbc':
                return 'c'
    else:
        return 'c'