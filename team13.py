team_name = 'team13'
strategy_name = 'Tit4Tat v63'
strategy_description = 'betray 70% of the time and collude 30% of the time.'

import random
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history) == 0:
        return 'b'
    elif 'c' in their_history(-1):  
        return 'b'
    elif 'b' in their_history(-1):
        return 'b'
    else:
        if random.random() < 0.70: 
            return 'b'         
        else:
            return 'c'             
    