board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
#가로 세로 대각선 확인

result = 0
pointx, pointy = 0, 0


def check_win(rock, ci, cj):
    steps = []

    #세로
    if 0 + 2 <= ci <= 19 - 2 - 1:
        cnt = 0
        for i in range(ci - 2, ci + 2 + 1):
            if board[i][cj] == rock:
                cnt += 1
        steps.append(cnt)
    #가로
    if 0 + 2 <= cj <= 19 - 2 - 1:
        cnt = 0
        for j in range(cj - 2, cj + 2 + 1):
            if board[ci][j] == rock:
                cnt += 1
        steps.append(cnt)

    #대각 \ / 
    if 0 + 2 <= ci <= 19 - 2 - 1 and 0 + 2 <= cj <= 19 - 2 - 1:
        # \
        cnt = 0 
        for k in range (-2, 3):
            if board[ci+k][cj+k] == rock:
                cnt+=1
        steps.append(cnt)

        #/
        cnt = 0
        for k in range(-2,3):
            if board[ci+k][cj-k] == rock:
                cnt+=1
        steps.append(cnt)

    if 5 in steps:
        return True
        
    

flag = False
for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            rock = board[i][j]
            #가로 세로 대각선 확인
            if check_win(rock, i, j):
                flag = True
                print(rock)
                print(i+1, j+1)

if flag == False:
    print(0)
            