def rotate(a:list,n:int):
    rotate = list()
    for i in range(n):
        rotate.insert((i+1)%n,a[i])
    return rotate


arr = [2,3,4,5,6,7]
arr = rotate(arr,len(arr))
print(arr)