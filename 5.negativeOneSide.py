def neg(a:list,n:int):
    j = 0
    for i in range(n):
        if (a[i] < 0):
            a[i],a[j] = a[j],a[i]
            j = j + 1
    return a

if __name__=="__main__":
    arr = [-1,-4,-6,-3,3,6,7,4,9,-10,-39,80]
    arr_size = len(arr)
    sorta = neg(arr,arr_size)
    print(sorta)