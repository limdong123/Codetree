gender = int(input()) #0 남자, 1 여자 
age = int(input())

if(gender):
    if(age >= 19):
        print("WOMAN")
    else:
        print("GIRL")
else:
    if(age >= 19):
        print("MAN")
    else:
        print("BOY")