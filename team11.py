
team_name = 'X2X' # Only 10 chars displayed.
strategy_name = "Double Crosser + Basic Counters"
strategy_description = 'Changes based on # of betrayals'
    
def move(my_history, their_history, my_score, their_score):
    
    if len(their_history) == 0:
        return 'c'
        
    if len(their_history) > 99:
        return 'b' 
         
    if their_history.count('b') > 2:
        return 'b'    
        
    elif 'c' not in their_history:
        return 'b'   
        
    elif 'b' not in their_history:
        return 'c'     
        
    elif my_history[-2] == their_history[-1]:
        return 'c' 
        
    elif their_history[0:4] == 'cbcb' or their_history[0:4] == 'bcbc':
        return 'b'  
             
    elif len(their_history) < 100: 
        if len(their_history) > 6:
            if 'b' not in their_history[:7]:
                 return 'c'
        
    else:
        return 'c'
        
    
        
    
    
    


