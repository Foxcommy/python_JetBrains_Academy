grid = input("Enter cells: ")
separator = '---------'

list_grid = list(grid)
center = list_grid[4]
empty_cell = list_grid.count('_')

print(separator)
for i in range(0, 3):
    print('| ' + list_grid[i * 3] + ' ' + list_grid[i * 3 + 1] + ' ' + list_grid[i * 3 + 2] + ' |')
print(separator)

win_x_row_board = 0
win_o_row_board = 0
win_x_col_board = 0
win_o_col_board = 0
win_x_dig_board = 0
win_o_dig_board = 0
impossible_cnt = 0

# check row winner
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
    print('Impossible')
elif win_list.count(0) == 6 and empty_cell != 0:
    print('Game not finished')
elif win_list.count(0) == 6 and empty_cell == 0:
    print('Draw')
elif win_x_row_board > 0 or win_x_col_board > 0 or win_x_dig_board > 0:
    print('X wins')
elif win_o_row_board > 0 or win_o_col_board > 0 or win_o_dig_board > 0:
    print('O wins')
