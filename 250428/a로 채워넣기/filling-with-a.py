st = input()

new_st1 = st.replace(st[1], "a",1)
new_st2 = new_st1.replace(st[-2], "a",1)
print(new_st2)