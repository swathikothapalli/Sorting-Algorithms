l=list(map(int, input().split(" ")))
for i in range(0,len(l)):
    for j in range(0,len(l)-1):
        if(l[j]>l[j+1]):
            l[j],l[j+1]=l[j+1],l[j]
print(l)
