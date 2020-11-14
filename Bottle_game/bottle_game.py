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
    if space_available!=4 and  bottle_state[d_bottle][last_d_bottle-1]==color: return "Not_possible_color_didnt_match"
    for i in range(space_available):
        if color==bottle_state[s_bottle][last_s_bottle-i]:
            color_count=i+1
        else:
            break
    for i in range(color_count):
        bottle_state[s_bottle][last_s_bottle-i]=None
        bottle_state[d_bottle][last_d_bottle+i]=color
    return bottle_state

        

print(Move(intitial_state,[2,10]))