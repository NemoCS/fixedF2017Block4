team_name = 'MemeLord' # Only 10 chars displayed.
strategy_name = 'Random Choices Unless Certain Circumstance'
strategy_description = 'This strategy randomly picks b or c unless in certain situations.'
    
def move(my_history, their_history, my_score, their_score):
    
    import random
    
    if random.random < 0.33 and len(my_history) == 0:
        return 'c'
    elif random.random > 0.33 and random.random < 0.66 and len(my_history) == 0:
        return 'b'
    elif random.random > 0.66 and their_history == 'c' and len(my_history) == 0:
        return 'b'
    elif random.random > 0.66 and their_history == 'b' and len(my_history) == 0:
        return random.choice(['c','b'])
        
    if random.random < 0.67 and len(my_history) > 0:
        return random.choice(['c','b'])
    elif len(my_history) > 0 and random.random > 0.67:
        return 'b' 