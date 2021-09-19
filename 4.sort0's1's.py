def sort0s(a,n):
    lo = 0
    hi = n - 1
    mid = 0
    while mid <= hi:
        if a[mid] == 0:
            a[lo], a[mid] = a[mid], a[lo]
            lo = lo + 1
            mid = mid + 1
        elif a[mid] == 1:
            mid = mid + 1
        else:
            a[mid], a[hi] = a[hi], a[mid]
            hi = hi - 1
    return a

    # Function to print array


def printArray(a):
    for k in a:
        print(k,end=" ")


if __name__ == "__main__":
    arr = [1,0,2,0,1,0,0,2,2,0,1,0,2,2,1]
    arr_size = len(arr)
    a = sort0s(arr,arr_size)
    print(a)
    printArray(a)