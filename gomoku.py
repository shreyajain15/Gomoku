"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Oct. 30, 2021
"""


def is_empty(board):
    for row in board:
        for col in row:
            if col == ' ':
                continue
            else:
                return False
    return True
    
    
def is_bounded(board, y_end, x_end, length, d_y, d_x):
    
    if (d_y == 0 and d_x == 1): #for left-to-right (0,1)

        try:
            lst = board[y_end][x_end - length: x_end +2]
        except :
            try:
                lst = board[y_end][x_end - length: x_end +1]
            except:
                try:
                    lst = board[y_end][x_end - length + 1: x_end +2]
                except:
                    lst = []

        check_lst = [' '] + board[y_end][x_end - length + 1 : x_end + 1] + [' ']
        print(check_lst)
        print(lst)
        if check_lst == lst:
            return 'OPEN'

        elif (check_lst[:len(check_lst)-1] == lst ) or  (check_lst[len(check_lst)+1:] == lst ) or (check_lst[:len(check_lst)-1] == lst[:len(lst)-1]) or  \
            ((check_lst[len(check_lst)+1:]) == lst[len(lst)+1:]):
            return 'SEMIOPEN'

        else:
            return 'CLOSED'

    elif (d_y == 1 and d_x == 0): # for Top to Bottom (1,0)

        try:
            y = y_end - length
            lst = []
            for i in range(length+2):
                lst += board[y][x_end]
                y += 1
        except :
            try:
                y = y_end - length + 1
                lst = []
                for i in range(length+1):
                    lst += board[y][x_end]
                    y += 1
            except:
                pass

            try:
                y = y_end - length
                lst = []
                for i in range(length+1):
                    lst += board[y][x_end]
                    y += 1
            except:
                lst = []

        y = y_end - length + 1
        check_lst = []
        for i in range (length):
            check_lst += board[y][x_end]
            y += 1

        check_lst = [' '] + check_lst + [' ']


        if check_lst == lst:
            return 'OPEN'

        elif (check_lst[:len(check_lst)-1] == lst ) or  (check_lst[len(check_lst)+1:] == lst ) or (check_lst[:len(check_lst)-1] == lst[:len(lst)-1]) or  \
            ((check_lst[len(check_lst)+1:]) == lst[len(lst)+1:]):
            return 'SEMIOPEN'

        else:
            return 'CLOSED'

        
    elif (d_y == 1 and d_x == 1): # for Upper-left to Lower-left (1,1)

        try:
            y = y_end - length 
            x = x_end - length 
            lst = []
            for i in range(length+2):
                lst += board[y][x]
                y += 1
                x += 1
        except :
            try:
                y = y_end - length + 1
                x = x_end - length + 1
                lst = []
                for i in range(length+1):
                    lst += board[y][x]
                    y += 1
                    x += 1
            except:
                try:
                    y = y_end - length
                    x = x_end - length
                    lst = []
                    for i in range(length+1):
                        lst += board[y][x]
                        y += 1
                        x += 1
                except:
                    lst = []

        y = y_end - length + 1
        x = x_end - length + 1
        check_lst = []
        for i in range (length):
            check_lst += board[y][x_end]
            y += 1
            x += 1

        check_lst = [' '] + check_lst + [' ']
        print(check_lst)
        print(lst)
        if check_lst == lst:
            return 'OPEN'

        elif (check_lst[:len(check_lst)-1] == lst ) or  (check_lst[len(check_lst)+1:] == lst ) or (check_lst[:len(check_lst)-1] == lst[:len(lst)-1]) or  \
            ((check_lst[len(check_lst)+1:]) == lst[len(lst)+1:]):
            return 'SEMIOPEN'

        else:
            return 'CLOSED'
    
    elif (d_y == 1 and d_x == -1): # Upper-right to Lower-right (1,-1)

        try:
            y = y_end - length
            x = x_end + length
            lst = []
            for i in range(length+2):
                lst += board[y][x]
                y += 1
                x -= 1
        except :
            try:
                y = y_end - length + 1
                x = x_end + length - 1
                lst = []
                for i in range(length+1):
                    lst += board[y][x]
                    y += 1
                    x -= 1
            except:
                try:
                    y = y_end - length
                    x = x_end + length
                    lst = []
                    for i in range(length+1):
                        lst += board[y][x]
                        y += 1
                        x -= 1
                except:
                    lst = []

        y = y_end - length + 1
        x = x_end + length - 1
        check_lst = []
        for i in range (length):
            check_lst += board[y][x_end]
            y += 1
            x -= 1

        check_lst = [' '] + check_lst + [' ']
        print(check_lst)
        print(lst)

        if check_lst == lst:
            return 'OPEN'

        elif (check_lst[:len(check_lst)-1] == lst ) or  (check_lst[len(check_lst)+1:] == lst ) or (check_lst[:len(check_lst)-1] == lst[:len(lst)-1]) or  \
            ((check_lst[len(check_lst)+1:]) == lst[len(lst)+1:]):
            return 'SEMIOPEN'

        else:
            return 'CLOSED'
        
    
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    import copy
    open_seq_count = 0
    semi_open_seq_count = 0
    check_lst, board_lst, check_lst_1 , check_lst_2 , check_lst_3, check_lst_4= [],[],[],[],[],[]
    
    for ele in range(length):
            check_lst.append(col)

    check_lst = [' ']+ check_lst + [' ']

    if col == 'w':
            check_lst_1 = check_lst.copy()
            check_lst_1.pop()
            check_lst_1.append('b')
            check_lst_2 = ['b'] + check_lst[1:]
            

    elif col == 'b':
        check_lst_1 = check_lst.copy()
        check_lst_1.pop()
        check_lst_1.append('w')
        check_lst_2 = ['w'] + check_lst[1:]

    
    check_lst_3 = ['e'] + check_lst[1:]

    check_lst_4 = check_lst[:len(check_lst)-1] + ['e']

    if (d_y == 0 and d_x == 1): # Left to Right (0,1)

        board_lst = board[y_start][x_start:]


    elif (d_y == 1 and d_x == 0): # Top to Bottom (1,0)

        for i in range(len(board)):
            board_lst += board[i][x_start]

    elif (d_y == 1 and d_x == 1): # Upper left to Lower Left

        if x_start == 0:
            for ele in range(len(board) - y_start):
                board_lst += board[y_start + ele][x_start + ele]

        elif y_start == 0:
            for ele in range(len(board) - x_start):
                board_lst += board[y_start + ele][x_start + ele]

        

    elif (d_y == 1 and d_x == -1): # Upper right to Lower right

        if x_start == len(board)-1:
            for ele in range(len(board) - y_start):
                board_lst += board[y_start + ele][x_start - ele]

        elif y_start == 0:
            for ele in range(x_start + 1):
                board_lst += board[y_start + ele][x_start - ele]

    lst_sequences, lst = [],[]
    for ele in range(len(board_lst)):
        if board_lst[ele] == col:
            lst += col        
            if ele>0:
                if board_lst[ele - 1] != col:
                    lst = [board_lst[ele - 1]] + lst[:]

            else:
                lst = ['e'] + lst[:]
                
            if ele != len(board_lst)-1:
                if board_lst[ele + 1] != col:
                    lst += [board_lst [ele + 1 ]]
                    lst_sequences.append(lst)
                    lst = []
            else:
                lst += ['e']
                lst_sequences.append(lst)
                lst = []
    
    for lst in lst_sequences:
        if check_lst == lst:
            open_seq_count += 1

        elif check_lst_1 == lst:
            semi_open_seq_count += 1

        elif check_lst_2 == lst:
            semi_open_seq_count += 1
            
        elif lst == check_lst_4 or lst == check_lst_3:
            semi_open_seq_count+= 1
    
    value = (open_seq_count, semi_open_seq_count)
    return value

def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0

    for i in range(len(board)): #left to right (0,1)
        value = detect_row(board, col, i , 0, length, 0, 1)
        open_seq_count += value[0]
        semi_open_seq_count += value[1]

    for i in range(len(board)): #top to bottom (1,0)
        value = detect_row(board, col, 0 , i, length, 1, 0)
        open_seq_count += value[0]
        semi_open_seq_count += value[1]

    for i in range(len(board)-1): #Upper Left to Lower Left (1,1)
        value = detect_row(board, col, 0 , i, length, 1, 1)
        open_seq_count += value[0]
        semi_open_seq_count += value[1]

    for i in range(1,len(board)-1): #Upper Left to Lower Left (1,1)
        value = detect_row(board, col, i , 0, length, 1, 1)
        open_seq_count += value[0]
        semi_open_seq_count += value[1]

    for i in range(len(board)-1): #Upper Right to Lower Right (1,-1)
        value = detect_row(board, col, i , len(board) - 1 , length, 1, -1)
        open_seq_count += value[0]
        semi_open_seq_count += value[1]

    for i in range(len(board)-1): #Upper Right to Lower Right(1,-1)
        value = detect_row(board, col, 0 , i, length, 1, -1)
        open_seq_count += value[0]
        semi_open_seq_count += value[1]
    
    return (open_seq_count, semi_open_seq_count)
    
def search_max(board):
    import copy
    found = False
    sample_board = copy.deepcopy(board)
    for row in range(len(sample_board)):
        for ele in range(len(board)):
            if board[row][ele] == ' ':
                move_y = row
                move_x = ele
                score_value = score(sample_board)
                found = True
                break
        if found == True:
            break
            

    for row in range(len(sample_board)):
        for ele in range(len(sample_board[row])):
            if sample_board[row][ele] == ' ':
                sample_board[row][ele] = 'b'
                check_score = score(sample_board)
                if check_score > score_value:
                    score_value = check_score
                    move_y = row
                    move_x = ele
                sample_board[row][ele] = ' '

    position = (move_y, move_x)
    return position
    
def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])


def detect_row2(board, col, y_start, x_start, length, d_y, d_x):
    import copy
    open_seq_count = 0
    semi_open_seq_count = 0
    closed = 0
    check_lst, board_lst, check_lst_1 , check_lst_2 , check_lst_3, check_lst_4,check_lst_5= [],[],[],[],[],[],[]
    
    for ele in range(length):
            check_lst.append(col)


    check_lst = [' ']+ check_lst + [' ']

    if col == 'w':
            check_lst_1 = check_lst.copy()
            check_lst_1.pop()
            check_lst_1.append('b')
            check_lst_2 = ['b'] + check_lst[1:]
            check_lst_5 = ['e'] + check_lst [1: len(check_lst)-1] + ['b']
            check_lst_6 = ['b'] + check_lst [1: len(check_lst)-1] + ['e']
            check_lst_8 = ['b'] + check_lst [1: len(check_lst)-1] + ['b']

    elif col == 'b':
        check_lst_1 = check_lst.copy()
        check_lst_1.pop()
        check_lst_1.append('w')
        check_lst_2 = ['w'] + check_lst[1:]
        check_lst_5 = ['e'] + check_lst [1: len(check_lst)-1] + ['w']
        check_lst_6 = ['w'] + check_lst [1: len(check_lst)-1] + ['e']
        check_lst_8 = ['w'] + check_lst [1: len(check_lst)-1] + ['w']

    
    check_lst_3 = ['e'] + check_lst[1:]
    check_lst_4 = check_lst[:len(check_lst)-1] + ['e']
    check_lst_7 = ['e'] + check_lst [1: len(check_lst)-1] + ['e']

    if (d_y == 0 and d_x == 1): # Left to Right (0,1)

        board_lst = board[y_start][x_start:]


    elif (d_y == 1 and d_x == 0): # Top to Bottom (1,0)

        for i in range(len(board)):
            board_lst += board[i][x_start]

    elif (d_y == 1 and d_x == 1): # Upper left to Lower Left

        if x_start == 0:
            for ele in range(len(board) - y_start):
                board_lst += board[y_start + ele][x_start + ele]

        elif y_start == 0:
            for ele in range(len(board) - x_start):
                board_lst += board[y_start + ele][x_start + ele]

        

    elif (d_y == 1 and d_x == -1): # Upper right to Lower right

        if x_start == len(board)-1:
            for ele in range(len(board) - y_start):
                board_lst += board[y_start + ele][x_start - ele]

        elif y_start == 0:
            for ele in range(x_start + 1):
                board_lst += board[y_start + ele][x_start - ele]

    lst_sequences, lst = [],[]
    for ele in range(len(board_lst)):
        if board_lst[ele] == col:
            lst += col        
            if ele>0:
                if board_lst[ele - 1] != col:
                    lst = [board_lst[ele - 1]] + lst[:]

            else:
                lst = ['e'] + lst[:]
                
            if ele != len(board_lst)-1:
                if board_lst[ele + 1] != col:
                    lst += [board_lst [ele + 1 ]]
                    lst_sequences.append(lst)
                    lst = []
            else:
                lst += ['e']
                lst_sequences.append(lst)
                lst = []
    
    for lst in lst_sequences:
        if check_lst == lst:
            open_seq_count += 1

        elif check_lst_1 == lst:
            semi_open_seq_count += 1

        elif check_lst_2 == lst:
            semi_open_seq_count += 1
            
        elif lst == check_lst_4 or lst == check_lst_3:
            semi_open_seq_count+= 1

        elif lst == check_lst_5 or lst == check_lst_6 or lst == check_lst_7 or check_lst_8 == lst:
            closed += 1
                
    
    value = (open_seq_count, semi_open_seq_count,closed)
    return value

def detect_rows2(board, col, length):
    open_seq_count, semi_open_seq_count, closed = 0, 0, 0

    for i in range(len(board)): #left to right (0,1)
        value = detect_row2(board, col, i , 0, length, 0, 1)
        open_seq_count += value[0]
        semi_open_seq_count += value[1]
        closed += value[2]

    for i in range(len(board)): #top to bottom (1,0)
        value = detect_row2(board, col, 0 , i, length, 1, 0)
        open_seq_count += value[0]
        semi_open_seq_count += value[1]
        closed += value[2]

    for i in range(len(board)-1): #Upper Left to Lower Left (1,1)
        value = detect_row2(board, col, 0 , i, length, 1, 1)
        open_seq_count += value[0]
        semi_open_seq_count += value[1]
        closed += value[2]

    for i in range(1,len(board)-1): #Upper Left to Lower Left (1,1)
        value = detect_row2(board, col, i , 0, length, 1, 1)
        open_seq_count += value[0]
        semi_open_seq_count += value[1]
        closed += value[2]

    for i in range(len(board)-1): #Upper Right to Lower Right (1,-1)
        value = detect_row2(board, col, i , len(board) - 1 , length, 1, -1)
        open_seq_count += value[0]
        semi_open_seq_count += value[1]
        closed += value[2]

    for i in range(len(board)-1): #Upper Right to Lower Right(1,-1)
        value = detect_row2(board, col, 0 , i, length, 1, -1)
        open_seq_count += value[0]
        semi_open_seq_count += value[1]
        closed += value[2]
        
    
    return (open_seq_count, semi_open_seq_count, closed)

def is_win(board):
    draw = False
    
    black = detect_rows2(board , 'b', 5)
    white = detect_rows2(board , 'w', 5)

    if black != (0,0,0):
        return 'Black won'

    if white != (0,0,0):
        return 'White won'
        
          
    for row in board: # Checks for Draw
        if draw == True:
            break
        for ele in row:
            if ele == ' ':
                draw = True
                return 'Continue playing'
                break
            
    else:
        return 'Draw'
    
         




def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
                


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
        

    
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res

        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res

        
            
            
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


  
            
if __name__ == '__main__':
    easy_testset_for_main_functions()
    some_tests()
    play_gomoku(8)
