import turtle as t
a=(int(input("请输入边数：")))
c=['red','blue','orange','green']
bc=15
for i in range(a):
    t.pencolor(c[i%4])
    t.forward(bc+i*5)
    t.left(90)