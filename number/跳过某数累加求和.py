n=input("请输入一个数：")
n=int(n)
m=0
for i in range(1,101):
    if (i==n):
        continue
    m=m+i
print(m)