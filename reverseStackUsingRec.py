def pushback(temp):
    arr.append(temp)
    global top
    top += 1
def popback():
    arr.pop()
    global top
    top -= 1
def sortStack():
    if len(arr) == 1:
        return
    temp = arr[top]
    popback()
    sortStack()
    insert(temp)
    return
def insert(temp):
    if top == 0 or arr[top] <= temp:
        pushback(temp)
        return
    val = arr[top]
    arr.pop()
    top -= 1
    insert(arr,temp,top)
    arr.append(val)
    return


global arr,top
arr = [1, 3, 4, 5, 7, 80, 6]
top = len(arr)-1
sortStack()
print(arr)

