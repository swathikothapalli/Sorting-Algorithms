l=list(map(int, input().split(" ")))
print("before sorting : ")
print(l)
for i in range(0,len(l)):
    mi=i
    for j in range(i+1,len(l)):
        if(l[j]<l[mi]):
            mi=j
    l[i],l[mi]=l[mi],l[i]
print("after sorting : ")
print(l)
