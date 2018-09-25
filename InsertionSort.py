def insertionSort(array):
    i = 1
    j = 0
    while i < len(array):
        j = 0
        while array[i] > array[j]:
            j+=1
        tmp = array[i]
        array[i] = array[j]
        array[j] = tmp
        i+=1
    return array

array = [2,3,1,67,4,55,65,34,2]
print(insertionSort(array))


