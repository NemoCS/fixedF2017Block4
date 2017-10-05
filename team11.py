
team_name = 'Brick Sprencer' # Only 10 chars displayed.
strategy_name = "DoubleCrosser*"
strategy_description = 'Changes based on # of betrayals'
    
def move(my_history, their_history, my_score, their_score, number_of_rounds):
    
    their_betrayals = 0
    
    if len(their_history) == 0:
        return 'c'
        
    if their_history[-1] == 'b':
        their_betrayals += 1

    if len(their_history) > (number_of_rounds - 3):
        return 'b'

    if len(their_history) < number_of_rounds:
        if len(their_history) > 6:
            if 'b' not in their_history[:7]:
                 return 'c'
                 
    if their_betrayals > 3:
        return 'b'

    else:
        return 'c'
        
    
        
    
    
    


