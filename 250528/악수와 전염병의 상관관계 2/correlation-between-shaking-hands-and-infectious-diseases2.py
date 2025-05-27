N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]

# Please write your code here.
# n -> 개발자 숫자, k -> 전염병 옯길수 있는 횟수, p ->처음 전염병 걸린 개발자 번호, T-> 횟수
result = [False] * (N+1) #0은 음성, 1은 양성
result[P] = True
cnt_arr = [0] * (N+1) #악수한 횟수

handshakes.sort() 
# handshakes[i][0] -> 시간 handshakes[i][1],handshakes[i][2] -> 약수하는 사람들

for i in range(T):
    target1 = handshakes[i][1]
    target2 = handshakes[i][2]

    if result[target1]: #target1이 감염이라면
        cnt_arr[target1] += 1
    if result[target2]:
        cnt_arr[target2] += 1
    
    #타겟 1은 감염이고 아직 K번 이하라면 타겟2를 감염시킴
    if cnt_arr[target1] <= K and result[target1]:
        result[target2] = True
    
    if cnt_arr[target2] <= K and result[target2]:
        result[target1] = True


for  i in range(1, N+1):
    if result[i]:
        print(1, end="")
    else:
        print(0, end="")


