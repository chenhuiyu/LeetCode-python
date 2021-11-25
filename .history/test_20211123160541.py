def infection(board, i, j, bool_ans):
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        bool_ans = False
        return
    if board[i][j] == "O":
        board[i][j] = "."
        infection(board, i + 1, j, bool_ans)
        infection(board, i, j + 1, bool_ans)
        infection(board, i - 1, j, bool_ans)
        infection(board, i, j - 1, bool_ans)


board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]

bool_board = [[0 for j in range(len(board[0]))] for i in range(len(board))]
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] == "O":
            print(i, j)
            bool_ans = True
            infection(board, i, j, bool_ans)
            print(i, j, bool_ans)
            board[i][j] = 1 if bool_ans is True else 0
