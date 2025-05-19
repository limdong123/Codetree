n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Please write your code here.
class Data:
    def __init__(self, name, height, weight):
        self.name = name
        self.h = height
        self.w = weight

datas = []
for i in range(5):
    datas.append(Data(name[i], height[i], weight[i]))

datas.sort(key = lambda x : x.name)
print("name")
for i in range(5):
    print(f"{datas[i].name} {datas[i].h} {datas[i].w}")
print()
datas.sort(key = lambda x : -x.h)
print("height")
for i in range(5):
    print(f"{datas[i].name} {datas[i].h} {datas[i].w}")