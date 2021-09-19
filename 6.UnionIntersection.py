def un(a:list,b:list,n:int,m:int):
    result = list()
    intersection = list()
    i,j=0,0
    while i<n and j<m:
        if a[i]<b[j]:
            result.append(a[i])
            i += 1
        elif a[i]>b[j]:
            result.append(b[j])
            j += 1
        else:
            result.append(a[i])
            intersection.append(a[i])
            i += 1
            j += 1
    while i<n:
        result.append(a[i])
        i += 1
    while j<m:
        result.append(b[j])
        j += 1
    return result,intersection




if __name__=="__main__":
    arr = [1,2,4,5,6,8,10,16,26,69,80]
    brr = [3,4,5,7,14,40,60,70]
    arr_size = len(arr)
    brr_size = len(brr)
    unionResult,intersection = un(arr,brr,arr_size,brr_size)
    print("union : ",unionResult,"\nIntersection : ",intersection)

