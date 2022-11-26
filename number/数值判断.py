a=input("a:")
a=int(a)
b=input("b:")
b=int(b)
c=input("c:")
c=int(c)
if(a>b and a>c):
    print("a最大")
elif(b>a and b>c):
    print("b最大")
else:
    print("c最大")