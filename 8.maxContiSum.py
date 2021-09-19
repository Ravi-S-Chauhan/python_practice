def maxContSum(arr,n):
    max_so_far = 0
    max_ending = 0
    for i in arr:
        max_ending = max_ending + i
        if max_ending < 0 :
            max_ending = 0
        elif (max_so_far < max_ending ):
            max_so_far = max_ending
    return max_so_far


arr = [-2,-3,4,-1,-2,1,5,-3]
sum = maxContSum(arr,len(arr))
print(sum)