n=int(input())
r1,r2=map(int,input().split())
target=int(input())
x=n
dm=[31,28,31,30,31,30,31,31,30,31,30,31]

mem=[]
for month in range(1,13):
    for days in range(1,dm[month-1]+1):
        a=((6-month)**2)+abs(days-15)
        mem.append(a)

room=[r2]*n

while(x!=0):
    su=0
    room[x-1]=r1
    for p in mem:
        if(p>n):
            su+=sum(room)
        else:
            su+=sum(room[:p])
    if(su>target):
        print(room.count(r1))
        break
    if(x==1 and su<target):
        print(n)
    x-=1