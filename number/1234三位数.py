a=("1234")
f=0
for b in a:
    for c in a:
        for d in a:
            if (b!=c and c!=d and b!=d):
                e=b+c+d
                f=f+1
                print(int(e))
print("总计",f)               