####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'The name the team gives to itself' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
    import random
    if len(their_history) == 0:
        if random.random() < .25:
            return 'b'
        else:
            return 'c'
    elif their_history[-1] == 'b':
        return 'b'
    elif their_history[-1] == 'c' and my_history[-1] == 'c':
        if random.random() < .1:
            return 'b'
        else:
            return 'c'
    elif their_history[-1] == 'c' and my_history[-1] == 'b':
        return 'b'    