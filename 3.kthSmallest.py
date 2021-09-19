def kthSmallest(arr:list,n:int):
    arr.sort()
    return arr[n-1]


if __name__=='__main__':
    arr = [12,45,74,85,24,8,35,68,42,5,853,22]
    arr_size = len(arr)
    k=5
    kthSmall = kthSmallest(arr,k)
    print("the kth smallest element is {}".format(kthSmall))
