####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Greedy Random'
strategy_name = 'Greedy Random'
strategy_description = '20 percent chance to collude'
    
def move(my_history, their_history, my_score, their_score):
    import random
    if random.random() > .8:
        return 'c'
    else:
        return 'b'
    