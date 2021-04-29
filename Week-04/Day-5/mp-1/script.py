##### TIC TAC TOE #####
# values record cells stat (X/O)
def gui_game(values):
    print("\n")
    print("\t*************")
    print("\t* {}  | {}  | {}  *".format(values[0],values[1],values[2]))
    print("\t*---|---|---*")
    print("\t* {}  | {}  | {}  *".format(values[3],values[4],values[5]))
    print("\t*---|---|---*")
    print("\t* {}  | {}  | {}  *".format(values[6],values[7],values[8]))
    print("\t*************")

# single player------------------------
def single_player(current_player):
    # scan position
    values = [' ' for x in range(9)]

    # store X/O
    player_pos = {'X':[],{'O':[]}

    # game loop
    while True:
        gui_game(values)
            
        try:
            print("Player ", cur_player, " turn. Which box? : ", end="")
            move = int(input()) 
        except ValueError:
            print("Wrong Input!!! Try Again")
            continue

        if move < 1 or move > 9:
            print("Wrong Input!!! Try Again")
            continue

        if values[move-1] != ' ':
            print("Place already filled. Try again!!")
            continue

        values[move-1] = current_player

        player_pos[current_player].append(move)

        if player_win(player_pos, current_player):
            gui_game(values)
            print("Player ", current_player, " Win!")
            return current_player
# check wins
        if check_draw(player_pos):
            gui_game("Draw !!!")
            return 'D'

        def player_win(player_pos, current_player):
        
            line = [[1,2,4],[4,5,6],[7,8,9],[1,4,7],[2,5,8]]

            for x in line:
                if all(y in player_pos[current_player] for y in x):
                    return True

            return False
# check draws
        def player_draw(player_pos):
            if len(player_pos['X'])+(len(player_pos['O'])) == 9:
                return True
            return False

        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'

            