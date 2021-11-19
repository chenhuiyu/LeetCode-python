def processing(board, row_i, col_j, row, col, bucket):
    # 如果来到最后一个，返回true
    if row_i == 8 and col_j == 8:
        return True
    next_i = row_i if col_j != 8 else row_i + 1
    next_j = col_j + 1 if col_j != 8 else col_j + 1
    # 不需要填
    if board[row_i][col_j] != '.':
        # 直接跳下一个
        return processing(board, next_i, next_j, row, col, bucket)
        # return processing(board, next_i, next_j, row, col, bucket)
    # 需要填
    else:
        k = 3 * (row_i // 3) + col_j // 3
        # 遍历填入数字1-9
        for n in range(1, 10, 1):
            # 通过限制数组剪枝
            if row[row_i][n - 1] == 0 and col[col_j][n - 1] == 0 and bucket[k][n - 1] == 0:
                # board[i][j]填入n，修改限制数组
                row[row_i][n - 1] = 1
                col[col_j][n - 1] = 1
                bucket[k][n - 1] = 1
                # 递归跳下一个
                board[row_i][col_j] = str(n)
                # print(processing(board, next_i, next_j, row, col, bucket))
                if processing(board, next_i, next_j, row, col, bucket) is True:
                    return True
                # 回复递归现场
                row[row_i][num - 1] = 0
                col[col_j][num - 1] = 0
                bucket[k][num - 1] = 0
                board[row_i][col_j] = "."
        return False


if __name__ == "__main__":
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    row = [[0 for i in range(9)] for j in range(9)]
    col = [[0 for i in range(9)] for j in range(9)]
    bucket = [[0 for i in range(9)] for j in range(9)]

    for i in range(9):
        for j in range(9):
            k = 3 * (i // 3) + j // 3
            if board[i][j] != ".":
                num = int(board[i][j])
                row[i][num - 1] = 1
                col[j][num - 1] = 1
                bucket[k][num - 1] = 1
    processing(board, 0, 0, row, col, bucket)