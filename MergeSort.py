def merge(l,left,mid,right):
    ll = l[left:mid+1]
    rl = l[mid+1:right+1]
    i=0
    j=0
    k=left
    while(i<len(ll) and j<len(rl)):
        if(ll[i]<rl[j]):
            l[k]=ll[i]
            i=i+1
        elif(rl[j]<ll[i]):
            l[k]=rl[j]
            j=j+1
        k=k+1
    while(i<len(ll)):
        l[k]=ll[i]
        i=i+1
        k=k+1
    while(j<len(rl)):
        l[k]=rl[j]
        j=j+1
        k=k+1

def mergesort(l,left,right):
    if(left<right):
        mid=(left+right)//2
        mergesort(l,left,mid)
        mergesort(l,mid+1,right)
        merge(l,left,mid,right)

l=list(map(int,input().split()))
mergesort(l,0,len(l)-1)
print(l)
