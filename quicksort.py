def quicksort(array, left, right):
    if(left>=right):
        return
    pivot = array[(left+right)//2]
    index = partition(array, pivot, left, right)
    quicksort(array,left,index-1)
    quicksort(array,index,right)
def partition(array, pivot, left, right):
    while(left<=right):
        while(array[left]<pivot):
            left = left+1
        while(array[right]>pivot):
            right = right-1
        if(left<=right):
            array[left],array[right]=array[right],array[left]
            left = left+1
            right = right-1
    return left
array = list(map(int,input().split()))
quicksort(array,0, len(array)-1)
print(array)
