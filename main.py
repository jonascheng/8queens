
QUEENS = 8

def print_board(board, size):
    for row in range(size):
        line = ""
        for col in range(size):
            if board[col] == row:
                line += " *|"
            else:
                line += "  |"
        print(line)

def is_valid(board, current):
    for col in range(current):
        if board[col] == board[current]: # place on the same row
            return False
        if current - col == abs(board[current] - board[col]): # place on diagonal
            return False
    return True

def queens(board, current, size):
    global sum
    if current == size: # reach the rightest col
        sum += 1
        print_board(board, size)
        return True
    else:
        for row in range(size):
            board[current] = row # place on current, row
            if is_valid(board, current):
                if queens(board, current+1, size): # process next col
                    # return True
                    pass
        return False

def solve_queens(size):
    board = [-1] * size # cols
    return queens(board, 0, size) # start from the leftest col

global sum
sum = 0

solve_queens(QUEENS)

print("total solutions: {}".format(sum))
