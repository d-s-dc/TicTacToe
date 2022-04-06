def print_config(config):
    print()
    for i in range(9):
        if config[i] == 1:
            char_val = 'X'
        elif config[i] == 2:
            char_val = 'O'
        else:
            char_val = ' '
        print('',char_val,'', end = '')
        if i != 2 and i != 5 and i!= 8:
            print('|', end = '')
        if i == 2 or i == 5:
            print('\n---|---|---')
    print("\n")

value_map = {1 : 10, 2 : -10}

final_pos = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

def final_check(config):
    for final_config in final_pos:
        if config[final_config[0]] == config[final_config[1]] and config[final_config[1]] == config[final_config[2]] and config[final_config[0]] != 0:
            return True, config[final_config[0]]
    return False, 0

def recursive_fun(config, turn):
    for final_config in final_pos:
        if config[final_config[0]] == config[final_config[1]] and config[final_config[1]] == config[final_config[2]] and config[final_config[0]] != 0:
            return None, value_map[config[final_config[0]]]
    count = [1 for i in config if i == 0]
    if not len(count):
        return None, 0
    max = -11
    min = 11
    fmove = None
    for idx, i in enumerate(config):
        if i == 0:
            temp = config.copy()
            temp[idx] = turn
            move, val = recursive_fun(temp.copy(), 3 - turn)
            if turn == 1 and val > max:
                max = val
                fmove = idx
            elif turn == 2 and val < min:
                min = val
                fmove = idx
    if turn == 1:
        to_return = max
    else:
        to_return = min
    return fmove, to_return

initial_config = [0,0,0,0,0,0,0,0,0]
print_config(initial_config)
turn = 1
while True:
    count = 0
    for i in initial_config:
        if i == 0:
            count += 1
    if count == 0:
        print("Match is a draw!")
        exit(-1)
    bool, player = final_check(initial_config)
    if bool:
        print_config(initial_config)
        print('Player', player, 'wins!')
        exit(-1)
    if turn == 1:
        mv, val = recursive_fun(initial_config.copy(), turn)
        print('Agent move', mv+1)
        initial_config[mv] = 1
        print_config(initial_config)
        turn = 3 - turn
    else:
        print('\nYour turn')
        move = int(input('Move - '))
        initial_config[move - 1] = 2
        print_config(initial_config)
        turn = 3 - turn