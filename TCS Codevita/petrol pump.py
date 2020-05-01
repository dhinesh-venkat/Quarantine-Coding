from random import sample as s

v=list(map(int,input().split()))
l=len(v)
n=[]
m=[]
while(l!=0):
    temp=0
    while(temp<500):
        take=s(v,l)
        rem=v.copy()
        for i in take:
            rem.remove(i)
        a=sum(take)
        b=sum(rem)
        diff=abs(a-b)
        if(diff<5):
            n.append(diff)
            m.append([max(a,b),min(a,b)])
        temp+=1
    l-=1
new=n.index(min(n))
print(m[new][0])