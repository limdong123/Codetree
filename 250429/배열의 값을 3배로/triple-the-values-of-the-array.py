#for문 이용
matrix = []
for _ in range(3):
    data = list(map(int, input().split()))
    matrix.append(data)

new_matrix = []
for i in range(3):
    data = []
    for j in range(3):
        data.append(matrix[i][j]*3)
    new_matrix.append(data)


for i in range(3):
    for j in range(3):
        print(new_matrix[i][j], end=" ")
    print()


#리스트 커프리헨션을 이용
# matrix = [list(map(int, input().split())) for _ in range(3)]

# new_matrix = [ 
#     [i*3 for i in j]
#     for j in matrix
#     ]

# for i in range(3):
#     for j in range(3):
#         print(new_matrix[i][j], end=" ")
#     print()