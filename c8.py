def palind(r):
    e=len(r)-1
    s=0
    while(s<e):
        if(r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True
r1=('w','o','w')
r2=(1,2,3,2,2,1)
if(palind(r1)):
    print("It is a flip-flop")
else:
    print("It is not a flip-flop")
if(palind(r2)):
    print("It is a flip-flop")
else:
    print("It is not a flip-flop")