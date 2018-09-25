
def partition(array):
    if len(array) == 1:
        return array
    l = len(array)/2
    left = partition(array[:l])
    right = partition(array[l:])
    return merge(left, right)

def merge(array1, array2):
    array = []
    i,j = 0,0
    while i < len(array1) and j < len(array2):
            if array1[i] <= array2[j]:
                array.append(array1[i])
                i+=1
            else:
                array.append(array2[j])
                j+=1
    array += array1[i:]
    array += array2[j:]
    return array


array = [1,4,7,2,2,3,4,6,77,6,78,89]
print(partition(array))
