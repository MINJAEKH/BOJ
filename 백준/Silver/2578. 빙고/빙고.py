#import sys
#input = sys.stdin.readline

def check_bingo(board) :
    bingo = 0
    # case 1 
    for row in range(5) :
        if board[row].count(0) == 5 :
            bingo += 1
    # case 2
    for col in range(5) :
        if [b[col] for b in board].count(0) == 5 :
            bingo += 1
    # case 3
    left_diag = [board[row][row] for row in range(5)]
    if left_diag.count(0) == 5 :
        bingo += 1
    # case 4
    right_diag = [board[row][4-row] for row in range(5)]
    if right_diag.count(0) == 5 :
        bingo += 1

    return bingo
    
board = [list(map(int, input().strip().split())) for _ in range(5)]
numbers = []
for _ in range(5) :
    numbers.extend(list(map(int, input().strip().split())))

for i in range(25) :
    for row in range(5) :
        for col in range(5) :
            if numbers[i] == board[row][col] :
                board[row][col] = 0

    results = check_bingo(board)
    if results >= 3 :
        print(i+1)
        break