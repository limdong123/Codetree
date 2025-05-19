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
class Data:
    def __init__(self, name, height, weight):
        self.name = name
        self.h = height
        self.w = weight

datas = []
for i in range(n):
    datas.append(Data(name[i], height[i], weight[i]))

datas.sort(key = lambda x : (x.h, -x.w))
for i in range(n):
    print(f"{datas[i].name} {datas[i].h} {datas[i].w}")