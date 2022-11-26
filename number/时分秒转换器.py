while 1:
    a=input("请输入总秒数（若要退出请输入“exit”）：")
    if (a=="exit"):
        break
    else:
        a=int(a)
        x=0
        f=0
        m=0
        x=a//3600
        f=(a-3600*x)//60
        m=a-3600*x-60*f
        print(x,"小时",f,"分钟",m,"秒")
