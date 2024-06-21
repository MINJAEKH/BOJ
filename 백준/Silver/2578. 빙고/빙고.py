def check_bingo(board : list) :
    bingo = 0
    # 행
    for row in range(5) :
        if board[row].count(0) == 5 :
            bingo += 1
    # 열
    for col in range(5) :
        if all(board[row][col] == 0 for row in range(5)):
            bingo += 1
    # 대각선
    if all(board[diagonal][diagonal] == 0 for diagonal in range(5)):
        bingo += 1
    #대각선
    if all(board[4-diagonal][diagonal] == 0 for diagonal in range(5)):
        bingo += 1

    return bingo

board = [list(map(int, input().split())) for _ in range(5)]
speaker = []
for _ in range(5) :
    speaker.extend(list(map(int, input().split())))


for i in range(25) :
    for row in range(5) :
        for col in range(5) :
            if speaker[i] == board[row][col] :
                board[row][col] = 0
    if i >= 11 :
        result = check_bingo(board)
        if result >= 3 :
            print(i+1)
            break