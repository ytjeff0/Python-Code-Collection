import turtle as t
l=[10,30,50,70,90,110,130,150]
c=['red','green','blue','purple']
for i in range(8):
    t.penup()
    t.goto(-10*i,-10*i)
    t.pendown()
    for n in range(4):
        t.pencolor(c[i%4])
        t.forward(l[i])
        t.left(90)