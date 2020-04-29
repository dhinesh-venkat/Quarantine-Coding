#Distributed Books a.k.a Dearrangements
def Books(n):
    a=[0 for i in range(n+1)]
    if(n>0):
        a[1]=0
        if(n>1):
            a[2]=1
    a[0]=1
    for i in range(3,n+1):
        a[i]=(i-1)*(a[i-1]+a[i-2])
    return a[n]
n=int(input())
print(Books(n))