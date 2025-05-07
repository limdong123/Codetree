a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.

def plus(a,c):
    print(f"{a} + {c} = {a+c}")

def minues(a,c):
    print(f"{a} - {c} = {a-c}")

def division(a,c):
    print(f"{a} / {c} = {a/c:.0f}")

def multi(a,c):
    print(f"{a} * {c} = {a*c}")

if(o == "+"):
    plus(a,c)
elif(o == "-"):
    minues(a,c)
elif(o == "/"):
    division(a,c)
elif(o == "*"):
    multi(a,c)
else:
    print(False)