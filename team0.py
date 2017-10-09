team_name = 'Alternator' # Only 10 chars displayed.
strategy_name = 'Betray every 2nd turn'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
    if len(their_history) % 2 == 0:
        return 'b'
    else:
        return 'c'

    
