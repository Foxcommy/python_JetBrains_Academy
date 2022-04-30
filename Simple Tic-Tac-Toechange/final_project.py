grid = '_________'
grid_matrix = [[grid[0], grid[1], grid[2]], [grid[3], grid[4], grid[5]], [grid[6], grid[7], grid[8]]]
game_status = 'Game not finished'


def print_board():
    print('---------')
    print('|', grid_matrix[0][0], grid_matrix[0][1], grid_matrix[0][2], '|')
    print('|', grid_matrix[1][0], grid_matrix[1][1], grid_matrix[1][2], '|')
    print('|', grid_matrix[2][0], grid_matrix[2][1], grid_matrix[2][2], '|')
    print('---------')

def game_analyzer(grid_matrix):
    list_grid = [grid_matrix[0][0], grid_matrix[0][1], grid_matrix[0][2], grid_matrix[1][0], grid_matrix[1][1], grid_matrix[1][2], grid_matrix[2][0], grid_matrix[2][1], grid_matrix[2][2]]
    center = grid_matrix[1][1]
    empty_cell_cnt = list_grid.count('_')
    win_x_row_board = 0
    win_o_row_board = 0
    win_x_col_board = 0
    win_o_col_board = 0
    win_x_dig_board = 0
    win_o_dig_board = 0
    impossible_cnt = 0
    for col in range(0, 9, 3):
        win_x = 0
        win_o = 0
        for row in range(0, 3):
            if list_grid[col + row] == 'X':
                win_x += 1
            elif list_grid[col + row] == 'O':
                win_o += 1
        if win_x == 3:
            win_x_row_board += 1
            continue
        elif win_o == 3:
            win_o_row_board += 1
            continue

    # check column winner
    for row in range(0, 3):
        win_x = 0
        win_o = 0
        for col in range(0, 9, 3):
            if list_grid[col + row] == 'X':
                win_x += 1
            elif list_grid[col + row] == 'O':
                win_o += 1
        if win_x == 3:
            win_x_col_board += 1
            continue
        elif win_o == 3:
            win_o_col_board += 1
            continue

    # check diagonal winner
    if (center == list_grid[0] and center == list_grid[8]) or (center == list_grid[2] and center == list_grid[6]):
        if center == 'X':
            win_x_dig_board += 1
        elif center == 'O':
            win_o_dig_board += 1

    win_list = [win_x_row_board, win_o_row_board, win_x_col_board, win_o_col_board, win_x_dig_board, win_o_dig_board]

    # check for impossible difference
    if abs(list_grid.count('X') - list_grid.count('O')) > 1:
        impossible_cnt += 1
    elif (win_x_row_board > 0 and win_o_row_board > 0) or (win_x_col_board > 0 and win_o_col_board > 0):
        impossible_cnt += 1

    # decision
    if impossible_cnt > 0:
        game_status = 'Impossible'
    elif win_list.count(0) == 6 and empty_cell_cnt != 0:
        game_status = 'Game not finished'
    elif win_list.count(0) == 6 and empty_cell_cnt == 0:
        game_status = 'Draw'
    elif win_x_row_board > 0 or win_x_col_board > 0 or win_x_dig_board > 0:
        game_status = 'X wins'
    elif win_o_row_board > 0 or win_o_col_board > 0 or win_o_dig_board > 0:
        game_status = 'O wins'

    return game_status

print_board()

turn = 0
while game_status == 'Game not finished':
    turn += 1
    x, y = input("Enter the coordinates: ").split()
    if x.isdigit() and y.isdigit():
        x = int(x) - 1
        y = int(y) - 1
        if not ((x >= 0 and x<= 2) and (y >= 0 and y<= 2)):
            print("Coordinates should be from 1 to 3!")
        else:
            if grid_matrix[x][y] == '_':
                if turn % 2 == 1:
                    grid_matrix[x][y] = 'X'
                else:
                    grid_matrix[x][y] = 'O'
                print_board()
                game_status = game_analyzer(grid_matrix)
                if game_status != 'Game not finished':
                    print(game_status)
            else:
                print('This cell is occupied! Choose another one!')
    else:
        print('You should enter numbers!')
