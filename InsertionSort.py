l=list(map(int,input().split()))
for i in range(1,len(l)):
    j=i-1
    k=l[i]
    while(j>=0 and l[j]>k):
        l[j+1]=l[j]
        j=j-1
    l[j+1]=k
print(l)
