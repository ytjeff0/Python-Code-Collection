def grid(a):
    if(a==1):
        return 1
    if(a==2):
        return 2
    else:
        s=2
        for i in range(a-1):
            s=s*2
        return s
a_list=[]
for i in range(1,65):
    a_list.append(grid(i))
s=0
for i in a_list:
    s=s+i
print(s)