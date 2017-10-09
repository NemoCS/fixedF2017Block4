
team_name = 'H@vvk$' 
strategy_name = 'Classified'
strategy_description = 'Classified?'
    
def move(my_history, their_history, my_score, their_score):
    if len(their_history) == 0:
        return 'b'
    if their_history == 'c':
        return 'c'
    else:
        return 'b'
    if 'c' not in their_history:
        return 'b'
