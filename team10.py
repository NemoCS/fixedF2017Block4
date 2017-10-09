####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Sow-awse' # Only 10 chars displayed.
strategy_name = 'Chicken'
strategy_description = "Basically you add the sow-ace to the chicken..."
    
def move(my_history, their_history, my_score, their_score):
    #peter and my, "Code" for recognizing eachother
    partner = "False"
    if len(my_history) == 0:
        return "c"
    if len(my_history) == 1:
        return "b"
    if len(my_history) == 2:
        return "b"
    if len(my_history) == 3:
        return "c"
    if len(my_history) == 4:
        return "c"
    if len(my_history) == 5:
        return "b"
    if len(my_history) == 6:
        return "c"
    if len(my_history) == 7:
        return "c"
    if len(my_history) == 8:
        return "c"
    if len(my_history) == 9:
        return "b"
    if len(my_history) == 10:
        return "c"
    if len(my_history) == 11:
        if my_history == their_history:
            return "c"
            partner = "True"
        else:
            partner = "False"
            if their_history[-1] == "b":
                return "b"
                #if they squeal on me, I squeal back, the worst that could happen is lose 250
            else:
                return "b"
                #if they dont squeal, I squeal. I get 100 points :)
    if len(my_history) >= 12:
        if partner == "True":
            return "c"
        else:
            #just some possible strategys and counters
            if their_history[1:10] == my_history[0:9]:
                return "c"
            elif their_history == len(their_history) * "b":
                return "b"
            elif their_history[0:4] == "cbcb" or their_history[0:4] == "bcbc":
                return their_history[-1]
            elif their_history[-1] == "b":
                return "b"
                #if they squeal on me, I squeal back, the worst that could happen is lose 250 
            else:
                return "b"
                #if they dont squeal, I squeal. I get 100 points :)   
    if len(my_history) == 134:
        return "c"


    
