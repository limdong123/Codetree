board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
#가로 세로 대각선 확인

result = 0
pointx, pointy = 0, 0

for i in range(19 - 5):
    for j in range(19 - 5):
        if board[i][j] != 0:
            rock = board[i][j]
            #가로 세로 대각선 확인

            ROW, CELL, DIAG, XDIAG = False, False, False, False
            
            for k in range(1, 5):
                if rock == board[i][j+k]:
                    ROW = True
                else:
                    ROW = False
                    break
            for k in range(1,5):
                if rock == board[i+k][j]:
                    CELL = True
                else : 
                    CELL = False
                    break
            for k in range(1,5):
                if rock == board[i+k][j+k]:
                    DIAG = True
                else :
                    DIAG = False
                    break

            for k in range(1,5):
                if rock == board[i+k][j-k]:
                    XDIAG = True
                else :
                    XDIAG = False
                    break

            if ROW:
                result = rock
                pointx = i 
                pointy = j + 2
            elif CELL:
                result = rock
                pointx = i + 2
                pointy = j
            elif DIAG:
                result = rock
                pointx = i + 2
                pointy = j + 2
            elif XDIAG:
                result = rock
                pointx = i + 2
                pointy = j - 2

print(result)
print(pointx + 1, pointy + 1)
            



