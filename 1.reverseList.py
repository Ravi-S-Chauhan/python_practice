def reverseList(A,start,end):
    while start<end:
        A[start],A[end] = A[end],A[start]
        start += 1
        end -= 1
A = [1,2,3,4,5,6]
reverseList(A,0,len(A)-1)
print("the reverse list is {}".format(A))
