def zhishu(a):
    for i in range(2,a):
        if (a%i==0):
            return 0
    return 1
sum=0
for i in range(2,101):
    if(zhishu(i)==1):
        sum=sum+i
print(sum)