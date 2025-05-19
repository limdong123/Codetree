n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.
#키를 기준으로 오름차순 정렬
class Man:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

mans = []
for i in range(n):
    mans.append(Man(name[i], height[i], weight[i]))

print(mans[0].name)