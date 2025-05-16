n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here.
#이름이 가장 느린사람 자료 출력
class User:
    def __init__(self, name = "", street_address = "", region = ""):
        self.name = name
        self.street_address = street_address
        self.region = region

user = []
for i in range(n): #클래스에 값 입력
    user.append(User(name[i], street_address[i], region[i]))

result_idx = 0
for i in range(1, n): # 클래스 이름 가장 큰 사람 찾기
    if user[i].name > user[i-1].name:
        result_idx = i

print(f"name {user[result_idx].name}")
print(f"addr {user[result_idx].street_address}")
print(f"city {user[result_idx].region}")