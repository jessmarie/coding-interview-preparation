
def swap(toBeSorted, low, high):
    lowElem = toBeSorted[low]
    toBeSorted[low] = toBeSorted[high]
    toBeSorted[high] = lowElem
    return toBeSorted

def quickSort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    pivot = arr[0]
    i = 1
    j = len(arr)-1
    while i <= j:
        if arr[i] > pivot & arr[j] < pivot:
            arr = swap(arr, i, j)
        if arr[i] < pivot:
            i += 1
        if arr[j] >= pivot:
            j -= 1
    return qs(arr[1:i]) + [pivot] + qs(arr[i:])


/*FOLLOWING CODE DOES NOT SORT IN PLACE*/
def qs(arr):
    if arr == [] or len(arr) == 1:
        return arr
    le = []
    ri = []
    pivot = arr[0]
    for x in arr:
        if x < pivot:
            le.append(x)
        if x > pivot:
            ri.append(x)
    return qs(le) + [pivot] + qs(ri)

testArray = [2,33,5, 88, 123, 13, 4, 55, 34, 23]
testArray2 = [2,33,5,12, 88, 123, 13, 4,2, 1, 2,1, 545, 34, 11, 1, 24, 344, 3, 44, 56]
sortedArray = quickSort(testArray)
sortedArray2 = quickSort(testArray2)
print("sortedArray=" + str(sortedArray))
print("sortedArray=" + str(sortedArray2))
