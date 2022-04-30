grid = input("Enter cells: ")
grid_matrix = [[grid[0], grid[1], grid[2]], [grid[3], grid[4], grid[5]], [grid[6], grid[7], grid[8]]]


def print_board():
    print('---------')
    print('|', grid_matrix[0][0], grid_matrix[0][1], grid_matrix[0][2], '|')
    print('|', grid_matrix[1][0], grid_matrix[1][1], grid_matrix[1][2], '|')
    print('|', grid_matrix[2][0], grid_matrix[2][1], grid_matrix[2][2], '|')
    print('---------')


print_board()

while True:
    x, y = input("Enter the coordinates: ").split()
    if x.isdigit() and y.isdigit():
        x = int(x) - 1
        y = int(y) - 1
        if not ((x >= 0 and x<= 2) and (y >= 0 and y<= 2)):
            print("Coordinates should be from 1 to 3!")
        else:
            if grid_matrix[x][y] == '_':
                grid_matrix[x][y] = 'X'
                print_board()
                break
            else:
                print('This cell is occupied! Choose another one!')
    else:
        print('You should enter numbers!')
