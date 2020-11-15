colors= ['black','violet','ggreen','dgreen','orange','pink','red','blue','dblue']

intitial_state={
    1:['black','violet','ggreen','orange'],
    2:['red','pink','pink','pink'],
    3:['blue','ggreen','violet','ggreen'],
    4:['dblue','blue','orange','black'],
    5:['black','blue','violet','dblue'],
    6:['dblue','blue','dgreen','pink'],
    7:['orange','red','violet','ggreen'],
    8:['red','dgreen','black','dgreen'],
    9:['red','dblue','orange','dgreen'],
    10:[None,None,None,None],
    11:[None,None,None,None]
}

def Move(bottle_state, command):
    """
    Verifies a move and give the new state if present 
    if state not present returns the reason for failure
    input: 
    __dict__ bottle_state
    __list__ command
    output:
    if worked __dict__ new state 
    if not worked __string__ reason for failure
    """
    s_bottle,d_bottle=command
    if bottle_state[s_bottle][0]==None: return 'Not_possible_source_bottle_empty' 
    if None not in bottle_state[d_bottle]: return 'Not_possible_destination_bottle_full' 
    if None not in bottle_state[s_bottle]:
        last_s_bottle=3 
    else:
        for i in range(4): 
            if bottle_state[s_bottle][i]==None:
                last_s_bottle=i-1
                break 
    for i in range(4):
        if bottle_state[d_bottle][3-i]==None: 
            last_d_bottle=3-i
    space_available= len(bottle_state[d_bottle][last_d_bottle:])
    
    color = bottle_state[s_bottle][last_s_bottle]
    if space_available!=4 and  bottle_state[d_bottle][last_d_bottle-1]!=color: return "Not_possible_color_didnt_match"
    for i in range(space_available):
        if color==bottle_state[s_bottle][last_s_bottle-i]:
            color_count=i+1
        else:
            break
    for i in range(color_count):
        bottle_state[s_bottle][last_s_bottle-i]=None
        bottle_state[d_bottle][last_d_bottle+i]=color
    is_bottle_of_same=0
    for i in bottle_state[d_bottle]:
        if i == color: is_bottle_of_same+=1
    if is_bottle_of_same==4 : del bottle_state[d_bottle]
    return bottle_state

def path_finder(bottle_state):
    """
    finds the possible path from the given bottle state 
    """
    return [(i,j) for j in bottle_state.keys() for i in bottle_state.keys() if (None in bottle_state[j])and(None!=bottle_state[i][0])]

def is_success(bottle_state):
    if len(bottle_state)==2:
        return True
    return False
def One_step(bottle_state,past_path):
    print()
    
    
    printable_past_path= [str(step[0])+"_"+str(step[1]) for step in past_path]
    new_steps = path_finder(bottle_state)
    for step in new_steps:
        past_path_copy=past_path.copy()
        print(past_path_copy)
        bottle_state_copy=bottle_state.copy()
        print(bottle_state_copy)
        bottle_state_copy=Move(bottle_state_copy,step)
        if type(bottle_state_copy).__name__ != 'dict':
            print(bottle_state_copy)

            del bottle_state_copy
        elif is_success(bottle_state_copy):
            past_path_copy+=step
            printable_past_path= [str(step[0])+"_"+str(step[1]) for step in past_path_copy]
            print("desierd path is:")
            for p in printable_past_path[:-1]:
                print(p,end=',')
            print(printable_past_path[-1])
            for k in bottle_state_copy.keys():
                print(k,bottle_state_copy[k])
        else:
            One_step(bottle_state_copy,past_path_copy+[step])

One_step(intitial_state,[])
            
    








#print(Move(Move(intitial_state,[2,10]),[6,10]))
print(path_finder(intitial_state))


