team_name = 'H@vvk$' 
strategy_name = 'Not telling you'
strategy_description = 'I\'m gonna win'
    
def move(my_history, their_history, my_score, their_score):
    
    if len(their_history) == 0:
        return 'b'
    elif their_history == 'c':
        return 'c'
    else:
        return 'b'
    if 'c' not in their_history:
        return 'b'

  # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.      
    
    
    
#http://wiki.c2.com/?PavlovStrategy