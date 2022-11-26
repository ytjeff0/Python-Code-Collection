while 1:
    a=input("请输入第一个数：")
    if (a=="exit"):
        break
    else:
        a=float(a)
        b=input("请输入第二个数：")
        b=float(b)
        s1=a+b
        s2=a-b
        s3=a*b
        s4=a/b
        s5=a**b
        s6=a//b
        s7=a%b
        print("a+b",s1)
        print("a-b",s2)
        print("a*b",s3)
        print("a/b",s4)
        print("a**b",s5)
        print("a//b",s6)
        print("a%b",s7)
