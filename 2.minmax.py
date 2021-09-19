class pair:
    def __init__(self):
        self.max = 0
        self.min = 0


def getMinMax(arr: list, n: int):
    minmax = pair()
    if n == 1:
        minmax.min = arr[0]
        minmax.max = arr[0]
    if arr[0] > arr[1]:
        minmax.max = arr[0]
        minmax.min = arr[1]
    else:
        minmax.max = arr[1]
        minmax.min = arr[0]
    for i in range(2, n):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]
    return minmax


if __name__ == '__main__':
    arr = [123, 4354, 6345, 234, 789, 24, 54688, 1451, 234]
    arr_size = len(arr)
    minmax = pair()
    minmax = getMinMax(arr,arr_size)
    print("min is {} and max is {}".format(minmax.min,minmax.max))
    print(type(minmax))
