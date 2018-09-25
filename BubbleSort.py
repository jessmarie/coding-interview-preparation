def bubbleSort(array):
    sorted = False
    i = 0
    while i < len(array)-1:
        if array[i] > array[i+1]:
            tmp = array[i]
            array[i] = array[i+1]
            array[i+1] = tmp
            sorted = True
        i+=1
    if sorted:
        return bubbleSort(array)
    else:
        return array

array = [1,4,7,2,2,3,4,6,77,6,78,89]
print(bubbleSort(array))