a=input("请输入您的身高")
a=int(a)
if(a>150):
    print("全票")
elif(120<=a<=150):
    print("半价票")
else:
    print("免票")